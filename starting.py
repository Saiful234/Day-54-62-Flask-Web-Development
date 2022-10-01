from amount import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<img src="{{url_for("static", filename="C:\Users\niyas\Pictures\giphy.gif")}}"/>'


def make_bold(args):
    return "<b>bye</b>"
def make_emphasis():

@app.route('/bye')
@make_bold
def bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!, You are years old."

@app.route("/<int:post_id>")
def post(post_id):
    return f"Post {post_id}"

if __name__ == "__main__":
    app.run(debug=True)

    # '<img src="{{ url_for("brid", val=val) }}" alt="Image Placeholder"  height="400" lows-rc="https://media.giphy.com/media/ByzzQxTAVOSn8JASBz/giphy.gif">'