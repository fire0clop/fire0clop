#!/usr/bin/env python3
"""Regenerate assets/metrics.svg and assets/langs.svg from live GitHub data.

Reads scripts/config.json, queries the GitHub REST API for commit counts,
release counts and language bytes across the owner's public repositories,
then rewrites the two stat cards and the matching alt text in README.md.

Run locally with:  GITHUB_TOKEN=$(gh auth token) python3 scripts/refresh_stats.py
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "scripts" / "config.json").read_text(encoding="utf-8"))
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

# GitHub's own language colours, plus the grey used for the "Other" bucket.
LANG_COLORS = {
    "Swift": "#F05138",
    "Python": "#3776AB",
    "Objective-C": "#438eff",
    "C": "#555555",
    "C++": "#f34b7d",
    "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Shell": "#89e051",
    "Ruby": "#701516",
    "Go": "#00ADD8",
    "Kotlin": "#A97BFF",
    "Java": "#b07219",
    "Dockerfile": "#384d54",
    "Makefile": "#427819",
    "Mako": "#7e858d",
}
OTHER_COLOR = "#5b6478"


def request(path, want_headers=False):
    url = path if path.startswith("http") else f"{API}/{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-stats-refresh")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode() or "null")
            return (body, dict(resp.headers)) if want_headers else body
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return ({}, {}) if want_headers else None
        raise


def paged(path):
    """Yield every item of a paginated collection."""
    url = f"{API}/{path}{'&' if '?' in path else '?'}per_page=100"
    while url:
        body, headers = request(url, want_headers=True)
        for item in body or []:
            yield item
        url = next_link(headers.get("Link", ""))


def next_link(link_header):
    match = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
    return match.group(1) if match else None


def commit_count(owner, repo):
    """Total commits on the default branch, read off the pagination Link header."""
    _, headers = request(f"repos/{owner}/{repo}/commits?per_page=1", want_headers=True)
    last = re.search(r'[?&]page=(\d+)>;\s*rel="last"', headers.get("Link", ""))
    if last:
        return int(last.group(1))
    body = request(f"repos/{owner}/{repo}/commits?per_page=1")
    return len(body or [])


def collect():
    owner = CONFIG["owner"]
    exclude = set(CONFIG["exclude"])
    repos = [
        r for r in paged(f"users/{owner}/repos?sort=updated")
        if not r["fork"] and not r["archived"] and r["name"] not in exclude
    ]

    commits = 0
    releases = 0
    languages = {}
    for repo in repos:
        name = repo["name"]
        commits += commit_count(owner, name)
        rel = sum(1 for _ in paged(f"repos/{owner}/{name}/releases"))
        if rel == 0:  # projects tagged without cutting a GitHub release
            rel = sum(1 for _ in paged(f"repos/{owner}/{name}/tags"))
        releases += rel
        for lang, size in (request(f"repos/{owner}/{name}/languages") or {}).items():
            languages[lang] = languages.get(lang, 0) + size

    return {
        "products": len(CONFIG["products"]),
        "commits": commits,
        "releases": releases,
        "repos": len(repos),
        "languages": languages,
    }


# --- SVG rendering ------------------------------------------------------------

SANS = "-apple-system,'Helvetica Neue','Inter',Arial,sans-serif"
MONO = "ui-monospace,'SF Mono','JetBrains Mono',Menlo,monospace"


def metrics_svg(stats):
    cards = [
        (f"{stats['products']}", "products shipped", 40),
        (f"{stats['commits']}", "commits", 40),
        (f"{stats['releases']}", "releases", 40),
        (CONFIG["platforms"], "platforms", 26),
    ]
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 104" width="1200" '
        f'height="104" fill="none" role="img" aria-label="{metrics_alt(stats)}">'
        '<defs><linearGradient id="acc" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#a855f7"/><stop offset="1" stop-color="#22d3ee"/>'
        "</linearGradient></defs>"
    ]
    for index, (value, label, size) in enumerate(cards):
        parts.append(
            f'<g transform="translate({index * 305} 0)">'
            '<rect width="285" height="104" rx="14" fill="#10131c" stroke="#222a3d"/>'
            f'<text x="142" y="58" text-anchor="middle" font-size="{size}" font-weight="800" '
            f'fill="url(#acc)" style="font-family:{SANS};">{value}</text>'
            '<text x="142" y="84" text-anchor="middle" font-size="13" letter-spacing="1" '
            f'fill="#8b98b5" style="font-family:{MONO};">{label}</text></g>'
        )
    return "".join(parts) + "</svg>\n"


def language_split(stats):
    """Top languages by bytes, with everything else folded into 'Other'."""
    total = sum(stats["languages"].values())
    if not total:
        return [], 0
    ranked = sorted(stats["languages"].items(), key=lambda kv: kv[1], reverse=True)
    top = ranked[: CONFIG["max_languages"] - 1]
    rest = sum(size for _, size in ranked[len(top):])
    split = [(name, size / total * 100, LANG_COLORS.get(name, OTHER_COLOR)) for name, size in top]
    if rest:
        split.append(("Other", rest / total * 100, OTHER_COLOR))
    return split, total


def langs_svg(stats):
    split, total = language_split(stats)
    if not split:
        return None

    bar_x, bar_w = 40.0, 1120.0
    bars, legend, cursor = [], [], 40.0
    offset = bar_x
    for name, pct, color in split:
        width = bar_w * pct / 100
        bars.append(f'<rect x="{offset:.1f}" y="30" width="{width:.1f}" height="26" fill="{color}"/>')
        offset += width
        label = f"{name} {pct:.0f}%"
        legend.append(
            f'<g transform="translate({cursor:.0f} 84)">'
            f'<rect width="12" height="12" rx="3" fill="{color}"/>'
            f'<text x="18" y="11" font-size="13" fill="#c7d4ea" style="font-family:{SANS};">'
            f'{name} <tspan fill="#8b98b5">{pct:.0f}%</tspan></text></g>'
        )
        cursor += 30 + len(label) * 7.2 + 25  # legend swatch + text + gutter

    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 108" width="1200" '
        f'height="108" fill="none" role="img" aria-label="{langs_alt(stats)}">'
        '<clipPath id="rc"><rect x="40" y="30" width="1120" height="26" rx="13"/></clipPath>'
        '<text x="40" y="18" font-size="13" letter-spacing="2" fill="#8b98b5" '
        f'style="font-family:{MONO};">LANGUAGES · {round(total / 1024):,}KB across '
        f'{stats["repos"]} repos</text>'
        f'<g clip-path="url(#rc)">{"".join(bars)}</g>{"".join(legend)}</svg>\n'
    )


# --- README alt text ----------------------------------------------------------

def metrics_alt(stats):
    return (
        f"{stats['products']} products · {stats['commits']} commits · "
        f"{stats['releases']} releases · {CONFIG['platforms'].replace(' · ', ' & ')}"
    )


def langs_alt(stats):
    split, _ = language_split(stats)
    return "Languages: " + ", ".join(f"{name} {pct:.0f}%" for name, pct, _ in split)


def update_readme(stats):
    readme = ROOT / "README.md"
    text = original = readme.read_text(encoding="utf-8")
    for asset, alt in (("metrics.svg", metrics_alt(stats)), ("langs.svg", langs_alt(stats))):
        text = re.sub(
            rf'(<img src="assets/{asset}"[^>]*?alt=")[^"]*(")',
            lambda m, alt=alt: m.group(1) + alt + m.group(2),
            text,
        )
    if text != original:
        readme.write_text(text, encoding="utf-8")
        return True
    return False


def write(path, content):
    target = ROOT / path
    if target.exists() and target.read_text(encoding="utf-8") == content:
        return False
    target.write_text(content, encoding="utf-8")
    return True


def main():
    stats = collect()
    print(json.dumps({k: v for k, v in stats.items() if k != "languages"}, indent=2))
    print("languages:", json.dumps(stats["languages"]))

    changed = write("assets/metrics.svg", metrics_svg(stats))
    langs = langs_svg(stats)
    if langs:
        changed |= write("assets/langs.svg", langs)
    changed |= update_readme(stats)
    print("changed" if changed else "up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
