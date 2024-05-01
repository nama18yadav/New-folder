from flask import Flask, redirect , url_for, render_template

app = Flask(__name__)

@app.route("/home")
def home(name):
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html",content = ["aman","manan","naman"])

if __name__ == "__main__":
    app.run(debug=True)
