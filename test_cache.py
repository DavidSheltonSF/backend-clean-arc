from flask import Flask, jsonify, request
from flask_caching import Cache
from time import sleep

config = {"DEBUG": True, "CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 10000}

app = Flask(__name__)
app.config.from_mapping(config)

cache = Cache(app)

dataBase = [
    {"id": 1, "name": "David", "password": "david123"},
    {"id": 2, "name": "Joana", "password": "jo123"},
    {"id": 3, "name": "Carla", "password": "ca123"},
]


def make_cache_key():
    body = request.get_json()
    return body


@app.route("/api/<int:s>")
@cache.memoize()
def index(s):
    sleep(s)
    return jsonify({"response": f"Done {s}s"})


@app.route("/api/users", methods=["GET"])
def get_user():

    user: dict = request.get_json()
    response = None

    key = f"User(id={user['id']}, name={user['name']})"
    print(cache.get_dict(key))

    if cache.get(key):
        return cache.get(key)

    print("esperando...")
    for u in dataBase:
        if u.get("id") == user.get("id") or u.get("name") == user.get("name"):
            response = u

    cache.set(key, response)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(port=5000)
