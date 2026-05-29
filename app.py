from flask import Flask, request, redirect, render_template
import sqlite3
import random
import string
import os

app = Flask(__name__)

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Initialize database
def init_db():
    conn = sqlite3.connect("data/urls.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls(
            short TEXT PRIMARY KEY,
            long TEXT
        )
    """)

    conn.close()

init_db()


# Home Page
@app.route("/", methods=["GET", "POST"])
def home():

    short_url = None

    if request.method == "POST":

        long_url = request.form["url"]

        # Generate random short code
        short = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6
            )
        )

        # Store in database
        conn = sqlite3.connect("data/urls.db")

        conn.execute(
            "INSERT INTO urls VALUES (?, ?)",
            (short, long_url)
        )

        conn.commit()
        conn.close()

        # Generate shortened URL
        short_url = request.host_url + short

    return render_template(
        "index.html",
        short_url=short_url
    )


# Redirect Route
@app.route("/<short>")
def redirect_url(short):

    conn = sqlite3.connect("data/urls.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT long FROM urls WHERE short=?",
        (short,)
    )

    row = cur.fetchone()

    conn.close()

    if row:
        return redirect(row[0])

    return "URL not found"


# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)