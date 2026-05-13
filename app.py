from flask import Flask, render_template, request
from password_checker import check_password_strength, suggest_password
import sqlite3
import hashlib

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (hash TEXT)")
    conn.commit()
    conn.close()

init_db()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route("/", methods=["GET", "POST"])
def home():
    strength = ""
    suggestion = ""
    password = ""

    if request.method == "POST":
        password = request.form["password"]

        # Strength check
        strength = check_password_strength(password)

        # Store hash silently (no message)
        if "❌" not in strength:
            hashed = hash_password(password)

            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM passwords WHERE hash=?", (hashed,))
            exists = cursor.fetchone()

            if not exists:
                cursor.execute("INSERT INTO passwords (hash) VALUES (?)", (hashed,))
                conn.commit()

            conn.close()

            # Suggest if weak
            if "Weak" in strength:
                suggestion = suggest_password()

    return render_template(
        "index.html",
        strength=strength,
        suggestion=suggestion,
        password=password
    )


if __name__ == "__main__":
    app.run(debug=True)