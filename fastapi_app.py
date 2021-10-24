from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()

# FastAPI は Pydantic という型バリデーションライブラリを同梱している。
# これを使ってリクエスト・レスポンスのパラメータの型を検証することが出来る。

# レスポンスとして返ってくる JSON をバリデーションするためのスキーマクラスを定義。
class User(BaseModel):
    name: str = Field(description="指名")
    age: int = Field(description="年齢", ge=0)  # 0以上の整数
    country: str = Field(description="出身国")


@app.get("/hello")
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

# FastAPI の場合はパスパラメータ・クエリパラメータ・ボディの全てが関数の引数として定義できる。


@app.post("/users/{name}", response_model=User)
def create_user(name: str, age: int = Query(None), body: dict = Body(None)):
    return {
        "name": name,
        "age": age,
        "country": body["country"],
    }
