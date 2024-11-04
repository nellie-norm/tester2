import requests
from flask import Flask, render_template, request
from datetime import datetime

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
    elif query.count("plus") == 2:
        words = query.split()
        num1 = int(words[2])
        num2 = int(words[4])
        num3 = int(words[6].replace("?", ""))
        result = str(add_numbers_twice(num1, num2, num3))
        return result
    elif "plus" in query:
        words = query.split()
        num1 = int(words[2])
        num2 = int(words[4].replace("?", ""))
        result = str(add_numbers(num1, num2))
        return result
    elif "multiplied" in query:
        words = query.split()
        num1 = int(words[2])
        num2 = int(words[5].replace("?", ""))
        result = str(multiply_numbers(num1, num2))
        return result
    elif "minus" in query:
        words = query.split()
        num1 = int(words[2])
        num2 = int(words[4].replace("?", ""))
        result = str(subtract_numbers(num1, num2))
        return result
    elif "primes" in query:
        words = query.split()
        num1 = int(words[7].replace(",", ""))
        num2 = int(words[8].replace(",", ""))
        num3 = int(words[9].replace(",", ""))
        num4 = int(words[10].replace(",", ""))
        num5 = int(words[11].replace("?", ""))
        result = str(identify_prime(num1, num2, num3, num4, num5))
        return result
    else:
        return "Unknown"


def add_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def subtract_numbers(num1, num2):
    return num1 - num2


def identify_prime(num1, num2, num3, num4, num5) -> list:
    primes = []
    for num in (num1, num2, num3, num4, num5):
        if is_prime(num):
            primes.append(str(num))
    return ", ".join(primes)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def add_numbers_twice(num1, num2, num3):
    return num1 + num2 + num3


@app.route("/extension")
def hello_github():
    return render_template("extension.html")


@app.route("/submitextension", methods=["POST"])
def submit_github():
    input_name = request.form.get("name")
    response = requests.get(f"https://api.github.com/users/{input_name}/repos")

    if response.status_code == 200:
        repos = response.json()
        repo_info = []

        for repo in repos:
            commits_url = (
                f"https://api.github.com/repos/{repo['full_name']}/commits")
            commits_response = requests.get(commits_url)
            if commits_response.status_code == 200:
                commits = commits_response.json()
                commit_info = [{
                    "sha": commit["sha"],
                    "message": commit["commit"]["message"],
                    "author": commit["commit"]["author"]["name"],
                    "date": datetime.strptime(
                        commit["commit"]["author"]["date"],
                        "%Y-%m-%dT%H:%M:%SZ"
                    ).strftime("%B %d, %Y")
                } for commit in commits]

                repo_info.append({
                    "name": repo["full_name"],
                    "updated_at": datetime.strptime(
                        repo["updated_at"], "%Y-%m-%dT%H:%M:%SZ"
                    ).strftime("%B %d, %Y"),
                    "owner": repo["owner"]["login"],
                    "commits": commit_info
                })

        return render_template(
            "extension_hello.html", name=input_name, repos=repo_info)
