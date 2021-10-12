from flask import Flask, request, make_response
import os

app = Flask(__name__)


@app.route("/users", methods=['GET'])
def list_users():
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


# arguments : num page et taille de la page
@app.route("/list_users_page", methods=['GET'])
def list_users_page():
    path = 'users'

    files = os.listdir(path)
    # array = []
    # for name in files:
    #     with open(f"users/{name}") as test:
    #         data = test.read()
    #         array.append(data.split("\n")[0] + " " + data.split("\n")[1])

    current_page = int(request.args.get("page"))
    size_page = int(request.args.get("size"))
    users_len = len(files)

    total_page = users_len / current_page

    test = files[(current_page-1) * size_page:((current_page-1) * size_page) + size_page]
    print(test)

    return make_response(" - ", 200)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8001,
        debug=True,
    )
