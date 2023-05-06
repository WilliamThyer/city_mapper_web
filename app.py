from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    First test func
    """
    return "Hello world!"
