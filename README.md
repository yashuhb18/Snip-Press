# SNIP·PRESS

A minimal URL shortener with a **neo-brutalist print-shop** frontend, built with **Flask**, **SQLite**, and **Docker**.

Paste a long link → get a short link → share it. No accounts, no extra services.

**Live repo:** [github.com/yashuhb18/Snip-Press](https://github.com/yashuhb18/Snip-Press)

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
| Deploy    | Docker            |

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
├── Dockerfile
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
| Port           | `5000`               | Set in `app.py` / Docker `EXPOSE` |
| Short code length | `6` characters    | Defined in `app.py`            |
| Database path  | `data/urls.db`       | Auto-created on first run      |

---

## Screenshots

_Add a screenshot of the UI here after running the app._

---

## Author

**Yashwanth H B** — [@yashuhb18](https://github.com/yashuhb18)

---

## License

This project is open source. Add a license file if you plan to distribute it publicly.
