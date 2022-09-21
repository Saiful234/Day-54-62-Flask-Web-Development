from amount import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/bye')
def bye():
    return "<h2>Bye</h2>"\

@app.route("/username/<name>")
def greet(name, age):
    return f"Hello {name}!, You are {age} years old."

# @app.route("/<int:post_id>")
# def post(post_id):
#     return f"Post {post_id}"

if __name__ == "__main__":
    app.run(debug=True)