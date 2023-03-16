import random

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/alpine")
def alpine():
    return render_template("alpine.html")


@app.route("/mouse-hover", methods=["GET", "POST"])
def mouse_hover():
    return "Mouse hover event caught"


@app.route("/mouse-click", methods=["GET", "POST"])
def mouse_click():
    return "Mouse click event caught"


@app.route("/polling", methods=["GET"])
def polling():
    return str(random.randint(1000, 100000))


@app.route("/add-list-item", methods=["GET"])
def add_list_item():
    item = str(random.randint(1000, 100000))
    return f"<li>{item}</li>"


@app.route("/search", methods=["POST"])
def search():
    data = {
        "one": "one",
        "two": "two",
        "three": "three",
        "four": "four",
        "five": "five",
    }
    req = request.form.get("search")
    if req.lower() in data:
        return f"Found: {data[req]}"
    return "Nothing found"


@app.route("/edit", methods=["GET", "PUT"])
def click_to_edit():
    user = {
        "name": "John",
        "age": 30,
    }
    if request.method == "GET":
        return f"""<form hx-put='/edit' hx-target='this' hx-swap='outerHTML'>
                  <div>
                    <label>Name</label>
                    <input class="form-control mb-2" type='text' name="name" value='{user['name']}'>
                  </div>
                  <div class='form-group'>
                    <label>Age</label>
                    <input class="form-control mb-2" type='number' name='age' value="{user['age']}">
                  </div>
                  <button class="btn btn-primary mt-2">Submit</button>
                  </form>"""

    else:
        user["name"] = request.form.get("name")
        user["age"] = request.form.get("age")
        return f"""<div hx-target="this" hx-swap="outerHTML">
                <div><label>Name</label>: {user['name']}</div>
                <div><label>Age</label>: {user['age']}</div>
                <button hx-get="/edit" class="btn btn-primary mt-2">Click To Edit</button>
                </div>"""


if __name__ == "__main__":
    app.run()
