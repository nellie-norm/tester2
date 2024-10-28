from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/query", methods=["GET"])
def process_query_route():
    query = request.args.get("q")
    return process_query(query)


def process_query(query: str):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif query == "asteroids":
        return "Unknown"
    elif "your name" in query:
        return "nn1524as3824"
    elif "plus" in query:
        words = query.split()
        num1 = int(words[2])
        num2 = int(words[4].replace("?", ""))
        return str(add_numbers(num1, num2))
    else:
        return "Unknown"


def add_numbers(num1, num2):
    return num1 + num2
