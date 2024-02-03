from functools import wraps

from apiflask import APIFlask
from flask import jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

from config import Config


app = APIFlask(__name__, title="Awesome GigaChat")
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "*"}})


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        token = header.split(" ")[1] if header else None
        if not token:
            return "", 400
        return f(*args, **kwargs)

    return wrapper


@app.get("/", defaults={"path": ""})
@app.get("/<path:path>")
def index(path=""):
    return app.send_static_file("index.html")


@app.get("/login")
@token_required
def login():
    return "", 200


@app.post("/gigachat")
@token_required
def gigachat():
    request_data = request.get_json()
    return jsonify({"answer": request_data["promt"]}), 201


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return error, 400


if __name__ == "__main__":
    app.run()
