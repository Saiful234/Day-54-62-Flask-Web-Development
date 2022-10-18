from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def input_guess():
    return '<h1> Guess a number between 0 and 9</h1>'

@app.route('/<int:guess_no>')
def random_guess(guess_no):
    random_number = random.randint(0, 9)
    if guess_no == random_number:
        return f"You got it right, You guessed{guess_no} and the answer is {random_number}"
    else:
        return f"Try again!, You guessed{guess_no} and answer is {random_number}"

if __name__ == "__main__":
    app.run(debug=True)