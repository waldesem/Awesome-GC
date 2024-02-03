import sqlite3

from apiflask import APIFlask, HTTPBasicAuth
from flask import current_app
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

from config import Config


app = APIFlask(__name__, title="Awesome GigaChat")
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "*"}})

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username: str, password: str):
    db = sqlite3.connect(current_app.config["DATABASE_URI"])
    cursor = db.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE username=? AND password=?",
        (username, password),
    )
    result = cursor.fetchone()
    if result:
        return username
    return None


@app.get("/", defaults={"path": ""})
@app.get("/<path:path>")
def index(path=""):
    return app.send_static_file("index.html")

@app.auth_required(auth)
@app.post("/gigachat")
def gigachat():
    return {"hello": "world"}


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return error, 400


def create_database():
    conn = sqlite3.connect(Config.DATABASE_URI)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    app.run()
