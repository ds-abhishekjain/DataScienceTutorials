from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World<h1>"

@app.route("/helloworld2")
def hello_world2():
    return "<h1>Hello, World2<h1>"

@app.route("/helloworld3")
def hello_world3():
    return "<h1>Hello, World3<h1>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
