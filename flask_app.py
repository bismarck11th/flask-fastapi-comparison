from fastapi import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    return {"Hello": "World"}


# POST /users/{name}?age={age}
# {
#     "country": {country}
# }
# 各パラメータはそれぞれリクエストの異なる箇所で指定。

# ・{name} : パスパラメータ
# ・{age} : クエリパラメータ
# ・{country} : ボディ


@app.route("/users/<name>", methods=["POST"])
def create_user(name):
    age = request.args.get("age", type=int)
    body = request.json

    return {
        "age": age,
        "name": name,
        "country": body["country"],
    }
