from amount import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<img scr="https://media.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif">'

@app.route('/bye')
def bye():
    return "<h2>Bye</h2>"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!, You are years old."

@app.route("/<int:post_id>")
def post(post_id):
    return f"Post {post_id}"

if __name__ == "__main__":
    app.run(debug=True)