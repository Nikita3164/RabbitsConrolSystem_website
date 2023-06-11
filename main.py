from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/main")
def index():
    return render_template("base.html")


@app.route("/setup")
def setup():
    return render_template("setup.html")


if __name__ == "__main__":
    app.run(debug=True)