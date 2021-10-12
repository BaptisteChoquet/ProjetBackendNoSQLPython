from flask import Flask, request, make_response
import os

app = Flask(__name__)


@app.route("/users", methods=['GET'])
def hello_world():
    path = 'users'

    files = os.listdir(path)
    obj = {"users": {}}
    for name in files:
        with open(f"users/{name}") as test:
            data = test.read()
            obj["users"][os.path.splitext(name)[0]] = {
                    "firstname": data.split("\n")[0],
                    "lastname": data.split("\n")[1]
                 }

    return obj


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8001,
        debug=True,
    )
