FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p data

ENV PORT=5000
ENV BEHIND_PROXY=true

EXPOSE 5000

# Production WSGI server (not Flask's dev server)
CMD gunicorn --bind 0.0.0.0:${PORT} --workers 2 --threads 4 --timeout 120 app:app
