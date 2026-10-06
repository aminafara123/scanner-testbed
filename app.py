"""Deliberately vulnerable demo app. Never deploy this."""
import hashlib
import sqlite3

from flask import Flask, request

import config

app = Flask(__name__)


@app.route("/user")
def get_user():
    # Planted: SQL injection via string concatenation
    username = request.args.get("name", "")
    conn = sqlite3.connect("users.db")
    rows = conn.execute(
        "SELECT id, name, email FROM users WHERE name = '" + username + "'"
    ).fetchall()
    return {"rows": rows}


@app.route("/calc")
def calc():
    # Planted: eval of user input
    expression = request.args.get("expr", "1+1")
    return {"result": eval(expression)}


@app.route("/register", methods=["POST"])
def register():
    # Planted: MD5 for password hashing
    password = request.form.get("password", "")
    digest = hashlib.md5(password.encode()).hexdigest()
    conn = sqlite3.connect("users.db")
    conn.execute(
        "INSERT INTO users (name, pw) VALUES (?, ?)",
        (request.form.get("name", ""), digest),
    )
    conn.commit()
    return {"ok": True}


if __name__ == "__main__":
    # Planted: debug server exposed on all interfaces
    app.run(host="0.0.0.0", port=5000, debug=True)
