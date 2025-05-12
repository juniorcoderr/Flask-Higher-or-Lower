from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route("/")
def home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2t5Njd1ZXEwaHp2eTR1c3k2M2xpdWk3czF1YmV4bDJnazhhOWtzayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/grDFHLDd6Bl9vDCr4Z/giphy.gif'/>"
    )


@app.route("/<int:number>")
def user_number(number):
    if number < random_number:
        return ("<h1>Too low, try again!</h1>"
                "<img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    elif number > random_number:
        return ("<h1>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    else:
        return ("<h1>You found it!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")


if __name__ == "__main__":
    app.run(debug=True)
