from amount import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/bye')
def bye():
    return "<h2>Bye</h2>"

@app.route("/<int:number>/<name>")
def greet(name, number):
    return f"Hello{name}, You are {number} years old."

if __name__ == "__main__":
    app.run(debug=True)