import random

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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


if __name__ == "__main__":
    app.run()
