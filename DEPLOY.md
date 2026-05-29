# Deploy SNIP·PRESS to the internet (HTTPS)

Localhost is only on your machine. To share the app with everyone you need:

1. **A host** that runs your Docker container 24/7  
2. **HTTPS** (platforms provide this automatically)  
3. **A public URL** like `https://snip-press.onrender.com`  
4. **Persistent storage** for SQLite (optional on free tiers — see below)

This project is already set up for production:

- **Gunicorn** WSGI server (not Flask’s dev server)  
- **`BEHIND_PROXY`** so shortened links use `https://` behind Render/Railway  
- **`render.yaml`** for one-click Render deploy  

---

## Recommended: Render (free HTTPS, connect GitHub)

Best for portfolios: connect your repo and get `https://your-app.onrender.com`.

### Steps

1. Push this repo to GitHub: [yashuhb18/Snip-Press](https://github.com/yashuhb18/Snip-Press)  
2. Sign up at [render.com](https://render.com)  
3. **New → Blueprint** → connect GitHub → select **Snip-Press**  
4. Render reads `render.yaml` and deploys the Docker service  
5. Wait for **Live** — open the URL (e.g. `https://snip-press-xxxx.onrender.com`)

### Custom domain (optional)

1. Render dashboard → your service → **Settings → Custom Domains**  
2. Add `short.yourdomain.com`  
3. Add the DNS records Render shows (CNAME)  
4. HTTPS certificate is issued automatically (Let’s Encrypt)

### SQLite on Render (important)

| Plan | Database behavior |
|------|-------------------|
| **Free** | `data/urls.db` may reset when the service redeploys or sleeps |
| **Paid + disk** | Uncomment `disk:` in `render.yaml`, redeploy — links persist |

For a demo/portfolio, free is fine. For production traffic, use a **persistent disk** or migrate to PostgreSQL later.

---

## Alternative: Railway (GitHub + volume for SQLite)

1. [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub**  
2. Select **Snip-Press**  
3. Railway detects `Dockerfile` automatically  
4. **Variables** → add `BEHIND_PROXY` = `true`  
5. **Volumes** → mount path `/app/data` (keeps SQLite across deploys)  
6. **Settings → Networking → Generate domain** → you get `https://….up.railway.app`

Railway gives HTTPS on the default domain with no extra setup.

---

## Alternative: Fly.io (Docker + volume)

```bash
# Install flyctl: https://fly.io/docs/hands-on/install-flyctl/
fly launch
fly volumes create snip_data --size 1
# Mount volume to /app/data in fly.toml, then:
fly secrets set BEHIND_PROXY=true
fly deploy
```

Fly provides `https://your-app.fly.dev` automatically.

---

## VPS (DigitalOcean / AWS EC2) — full control

For a “real” server you manage:

1. Rent a small VPS (e.g. DigitalOcean Droplet, $4–6/mo)  
2. Install Docker  
3. Run with a volume and reverse proxy:

```bash
git clone https://github.com/yashuhb18/Snip-Press.git
cd Snip-Press
docker build -t snip-press .
docker run -d --restart unless-stopped \
  -p 127.0.0.1:5000:5000 \
  -v snip-data:/app/data \
  -e BEHIND_PROXY=true \
  --name snip-press snip-press
```

4. Point **Nginx** or **Caddy** at `localhost:5000` and terminate HTTPS (Caddy gets free certs automatically).

Example Caddyfile:

```text
short.yourdomain.com {
    reverse_proxy localhost:5000
}
```

---

## Checklist: “full stack” vs localhost

| Item | Localhost | Production |
|------|-----------|------------|
| URL | `http://localhost:5000` | `https://your-app.onrender.com` |
| HTTPS | No | Yes (platform or Caddy) |
| Server | Flask dev / gunicorn | Gunicorn in Docker |
| Short links | `http://localhost:5000/abc` | `https://your-domain.com/abc` |
| Database | `data/urls.db` | Same file + volume on host |
| Public access | Only you | Anyone on the internet |

---

## After deploy — test

1. Open your `https://…` URL  
2. Shorten `https://example.com`  
3. Confirm the result link starts with **`https://`** (not `http://`)  
4. Click the short link — it should redirect to example.com  

If short links show `http://`, ensure `BEHIND_PROXY=true` is set on the host.

---

## Free tier notes

- **Render free**: service sleeps after ~15 min idle; first visit may take 30–60s to wake  
- **Railway**: limited monthly credits on free trial  
- For always-on + persistent DB, use a paid plan or a small VPS  

---

## Add “Live demo” to README

Once deployed, put your URL at the top of `README.md`:

```markdown
**Live demo:** https://your-app.onrender.com
```

That turns the repo from a localhost project into a portfolio full-stack deployment.
