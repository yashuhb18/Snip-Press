# SNIP·PRESS

A minimal URL shortener with a **neo-brutalist print-shop** frontend, built with **Flask**, **SQLite**, and **Docker**.

Paste a long link → get a short link → share it. No accounts, no extra services.

**Repository:** [github.com/yashuhb18/Snip-Press](https://github.com/yashuhb18/Snip-Press)  
**Live demo:** _Deploy once — add your URL here (see [DEPLOY.md](DEPLOY.md))_

---

## Features

- Shorten any URL from a single-page UI
- Instant redirects via `/{short-code}`
- SQLite persistence (`data/urls.db`)
- Copy-to-clipboard on the result ticket
- Responsive layout (desktop + mobile)
- Fully containerized with Docker

---

## Tech stack

| Layer      | Technology        |
|-----------|-------------------|
| Backend   | Python 3.11, Flask 3 |
| Database  | SQLite            |
| Frontend  | HTML, CSS, vanilla JS |
| Deploy    | Docker, Gunicorn  |
| Production | Render / Railway / Fly.io / VPS |

---

## Go live (HTTPS for everyone)

Localhost only runs on your PC. To make this a **public full-stack app** with `https://`:

1. Use a cloud host (Render is the easiest — free HTTPS URL included).
2. Connect your GitHub repo and deploy the `Dockerfile`.
3. Set `BEHIND_PROXY=true` so short links use `https://your-domain.com/...`.

**Step-by-step guide:** [DEPLOY.md](DEPLOY.md)

**Fast path (Render):**

1. Sign up at [render.com](https://render.com)  
2. **New → Blueprint** → connect **Snip-Press** on GitHub  
3. Deploy → open `https://snip-press-xxxx.onrender.com`  

Optional: add a custom domain in Render settings — SSL is automatic.

---

## Quick start (Docker)

**Prerequisites:** [Docker](https://docs.docker.com/get-docker/) installed

```bash
git clone https://github.com/yashuhb18/Snip-Press.git
cd Snip-Press

docker build -t snip-press .
docker run -p 5000:5000 snip-press
```

Open **http://localhost:5000**, paste a URL, and click **STAMP SHORT LINK**.

To keep the database between container restarts, mount a volume:

```bash
docker run -p 5000:5000 -v snip-data:/app/data snip-press
```

---

## Local development (without Docker)

**Prerequisites:** Python 3.11+

```bash
git clone https://github.com/yashuhb18/Snip-Press.git
cd Snip-Press

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Visit **http://localhost:5000**.

---

## How it works

1. **POST /** — User submits a long URL; the app generates a random 6-character code and stores `short → long` in SQLite.
2. **GET /{short}** — Looks up the code and redirects to the original URL, or returns `URL not found`.

Short links use your server host, e.g. `http://localhost:5000/aB3xY9`.

---

## Project structure

```
Snip-Press/
├── app.py                 # Flask routes & SQLite logic
├── requirements.txt
├── Dockerfile             # Production image (Gunicorn)
├── render.yaml            # Render.com blueprint
├── DEPLOY.md              # Full deployment guide (HTTPS)
├── .env.example
├── templates/
│   └── index.html         # Main UI (Jinja2)
├── static/
│   ├── style.css          # Neo-brutalist styles
│   └── favicon.svg
└── data/                  # Created at runtime (gitignored)
    └── urls.db
```

---

## Configuration

| Setting        | Default              | Notes                          |
|----------------|----------------------|--------------------------------|
| Port           | `5000`               | Override with `PORT` env on cloud hosts |
| Short code length | `6` characters    | Defined in `app.py`            |
| Database path  | `data/urls.db`       | Auto-created on first run; use a volume in production |
| `BEHIND_PROXY` | unset (local)        | Set `true` on Render/Railway/Fly for correct HTTPS short URLs |
| Server (prod)  | Gunicorn             | Started via `Dockerfile`       |

---

## Screenshots

_Add a screenshot of the UI here after running the app._

---

## Author

**Yashwanth H B** — [@yashuhb18](https://github.com/yashuhb18)

---

## License

This project is open source. Add a license file if you plan to distribute it publicly.
