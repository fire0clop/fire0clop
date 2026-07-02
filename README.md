<p align="center">
  <img src="assets/hero.svg" alt="Egor Fomenko — iOS & Backend Engineer" width="100%">
</p>

<p align="center">
  <em>I design and build <b>complete mobile products</b> end to end —<br/>
  native <b>Swift / SwiftUI</b> clients on async <b>Python / FastAPI</b> backends, from database to App Store.</em>
</p>

<p align="center">
  <a href="mailto:egor555fomenko@gmail.com"><img src="https://img.shields.io/badge/Email-0b0b14?style=for-the-badge&logo=gmail&logoColor=d4af37" alt="Email"></a>
  <a href="https://www.linkedin.com/in/egor-fomenko-7620712a1"><img src="https://img.shields.io/badge/LinkedIn-0b0b14?style=for-the-badge&logo=linkedin&logoColor=22d3ee" alt="LinkedIn"></a>
  <img src="https://img.shields.io/badge/iOS_·_macOS-0b0b14?style=for-the-badge&logo=apple&logoColor=e5e7eb" alt="Apple platforms">
</p>

<p align="center">
  <img src="assets/metrics.svg" width="100%" alt="6 products · 164 commits · 36 releases · iOS & macOS">
</p>

<p align="center">
  <img src="assets/divider.svg" width="82%" alt="">
</p>

<h3 align="center">✦&nbsp;&nbsp;ABOUT&nbsp;&nbsp;✦</h3>

I'm a **solo full-stack mobile engineer** — I take a product from an empty repository to the App Store: the FastAPI backend, its database and realtime layer, the deployment, and a polished native SwiftUI client on top. I don't hand a spec to anyone; I design the data model, build the API, make WebSockets / packet tunnels / calls actually work on-device, and ship.

Across 2026 I shipped **six apps in very different domains** — real-time messaging with 1:1 WebRTC calls, a NetworkExtension VPN, a server-authoritative multiplayer game, and AI-assisted health and habit apps. Different problems, same discipline: own the whole stack, keep it fast, make it feel native.

Beyond mobile, I write **business-process automation** in Python — email/ticketing bots, ETL and data pipelines — and build **full-stack web apps** (Angular · Node/Express · .NET · PostgreSQL) for clients, from spec to a deployed server.

<h3 align="center">✦&nbsp;&nbsp;WHAT I BUILD&nbsp;&nbsp;✦</h3>

| Layer | What that means in my projects |
|-------|--------------------------------|
| **Native Apple** | SwiftUI for iOS & macOS · `NetworkExtension` packet tunnels · WebRTC + CallKit + PushKit calling · Keychain, offline caches, background tasks |
| **Async backends** | FastAPI · async SQLAlchemy 2.0 · WebSockets with Redis pub/sub fan-out · JWT + TOTP 2FA · Celery / ARQ / APScheduler workers |
| **Data & infra** | PostgreSQL + PostGIS · Redis · S3 / MinIO · Alembic migrations · Docker Compose · GitHub Actions CI |
| **AI** | Anthropic Claude — guided flows, multilingual generation (ru / en / es), correlation insights |

<h3 align="center">✦&nbsp;&nbsp;FEATURED WORK&nbsp;&nbsp;✦</h3>

<p align="center"><sub>Native app · API · realtime · infra — click any banner to open the repo.</sub></p>

<a href="https://github.com/fire0clop/siberia"><img src="assets/siberia.svg" alt="Siberia — Telegram-class messenger with WebRTC calls" width="100%"></a>
<a href="https://github.com/fire0clop/joker"><img src="assets/joker.svg" alt="Joker — server-authoritative multiplayer card game" width="100%"></a>
<a href="https://github.com/fire0clop/top-vpn"><img src="assets/top-vpn.svg" alt="Top-VPN — geo split-tunnel VPN for iOS & macOS" width="100%"></a>
<a href="https://github.com/fire0clop/klio"><img src="assets/klio.svg" alt="Klio — AI goal-tracking diary with Claude insights" width="100%"></a>
<a href="https://github.com/fire0clop/medoed"><img src="assets/medoed.svg" alt="Medoed — diabetes companion" width="100%"></a>
<a href="https://github.com/fire0clop/activity"><img src="assets/activity.svg" alt="Activity — location-based meetups & realtime chat" width="100%"></a>

<h3 align="center">✦&nbsp;&nbsp;SHIPPING TIMELINE&nbsp;&nbsp;✦</h3>

<p align="center">
  <img src="assets/timeline.svg" width="100%" alt="Project timeline across 2026 — six overlapping products">
</p>

<h3 align="center">✦&nbsp;&nbsp;SELECTED ENGINEERING&nbsp;&nbsp;✦</h3>

**[Siberia](https://github.com/fire0clop/siberia) — a messenger, not a chat demo**
- 1:1 **WebRTC** voice/video with CallKit + PushKit VoIP and a coturn TURN template
- `/ws` channels with heartbeat and **Redis pub/sub fan-out** across instances; per-chat monotonic `sync_seq` catch-up so clients never miss a message
- Group chats, broadcast channels, S3 media with thumbnails and presigned URLs, PostgreSQL full-text search, **TOTP 2FA**, offline cache + reconnect gap recovery

**[Top-VPN](https://github.com/fire0clop/top-vpn) — a real packet tunnel**
- `NEPacketTunnelProvider` embedding **sing-box** via Libbox, memory capped at **45 MB** to survive iOS jetsam
- **VLESS + Reality** (uTLS Chrome fingerprint, vision flow) with client-side `urltest` auto-rotation across an endpoint pool
- Geo **split-tunneling** (RU-direct / foreign-proxy), split DNS, an antizapret domain pipeline compiled to on-device `.srs` rule-sets — shipped on **iOS *and* macOS**

**[Joker](https://github.com/fire0clop/joker) — server-authoritative game engine**
- Full "Козёл" rules engine — 38-card deck with dual jokers, bidding constraints, trick resolution, штанга penalties and per-pulka scoring — all resolved **on the server**
- Realtime table over WebSockets + Redis, private rooms with stake-tiered matchmaking and bot fills
- **ELO** ranking across six leagues, a zero-sum chip economy with a transaction ledger, Celery timers and anti-collusion logging

**[Klio](https://github.com/fire0clop/klio) · [Medoed](https://github.com/fire0clop/medoed) · [Activity](https://github.com/fire0clop/activity) — product surface**
- **Klio:** a goal taxonomy with streak scheduling and **Anthropic Claude** driving guided goal creation and multilingual (ru/en/es) daily insight cards
- **Medoed:** an insulin **bolus calculator** (ISF/IC ratios) over a carb-counting dish library and meal diary, with Sign in with Apple + Google
- **Activity:** a **PostGIS** proximity feed with cursor pagination, join/waitlist logic, WebSocket group chat and APNs + FCM push

<h3 align="center">✦&nbsp;&nbsp;AUTOMATION &amp; WEB&nbsp;&nbsp;✦</h3>

<p align="center"><sub>Beyond mobile — business automation and full-stack web, from spec to production.</sub></p>

<a href="https://github.com/fire0clop/mail-ops-bot"><img src="assets/mail-ops-bot.svg" alt="Mail-Ops Bot — email → ticket → Telegram support-desk automation" width="100%"></a>

<p align="center"><sub>Also full-stack web for clients — Angular · Node/Express · .NET · PostgreSQL — and Python data pipelines (kept in private repos; happy to walk through them).</sub></p>

<h3 align="center">✦&nbsp;&nbsp;TECH ARSENAL&nbsp;&nbsp;✦</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white" />
  <img src="https://img.shields.io/badge/SwiftUI-0A84FF?style=flat-square&logo=swift&logoColor=white" />
  <img src="https://img.shields.io/badge/Combine-8E44AD?style=flat-square&logo=swift&logoColor=white" />
  <img src="https://img.shields.io/badge/NetworkExtension-1D1D1F?style=flat-square&logo=apple&logoColor=white" />
  <img src="https://img.shields.io/badge/WebRTC-333333?style=flat-square&logo=webrtc&logoColor=white" />
  <img src="https://img.shields.io/badge/CallKit-000000?style=flat-square&logo=apple&logoColor=white" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white" />
  <img src="https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white" />
  <img src="https://img.shields.io/badge/Alembic-6BA81E?style=flat-square&logo=python&logoColor=white" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/PostGIS-336791?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Anthropic_Claude-D4A27F?style=flat-square&logo=anthropic&logoColor=white" />
</p>

<p align="center">
  <img src="assets/langs.svg" width="82%" alt="Languages: Swift 51%, Python 37%, other 12%">
</p>

<h3 align="center">✦&nbsp;&nbsp;LET'S TALK&nbsp;&nbsp;✦</h3>

<p align="center">
  Open to <b>iOS / backend / full-stack</b> roles and freelance builds.<br/>
  If you need a product taken from idea to the App Store by one person who owns the whole stack — let's talk.
</p>

<p align="center">
  <a href="mailto:egor555fomenko@gmail.com"><img src="https://img.shields.io/badge/egor555fomenko@gmail.com-0b0b14?style=for-the-badge&logo=gmail&logoColor=d4af37" alt="Email"></a>
  <a href="https://www.linkedin.com/in/egor-fomenko-7620712a1"><img src="https://img.shields.io/badge/LinkedIn-0b0b14?style=for-the-badge&logo=linkedin&logoColor=22d3ee" alt="LinkedIn"></a>
</p>

<p align="center">
  <img src="assets/divider.svg" width="82%" alt="">
</p>

<p align="center"><sub>◈ &nbsp; Built end to end — Swift on the surface, FastAPI underneath. &nbsp; ◈</sub></p>
