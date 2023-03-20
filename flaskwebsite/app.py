from flask import Flask, render_template
from flask_navigation import Navigation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")

if __name__ == '__main__':
    app.run(debug=True)
