from flask import Flask
import random

app = Flask(__name__)

MOTIVATION_QUOTES = [
    "Ship small, ship often – DevOps in action.",
    "Automate the boring stuff; focus on value – DevOps mindset.",
    "If it hurts, do it more often – DevOps continuous delivery.",
    "You build it, you run it – DevOps responsibility.",
    "Tests passing? Ship it with confidence – the power of DevOps CI/CD.",
]


@app.route("/")
def hello():
    return "Hello, DevOps World!"


@app.route("/motivator")
def motivator():
    return random.choice(MOTIVATION_QUOTES)


if __name__ == "__main__":
    app.run()
