"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greeting')
def greet_person():
    """Ask user if they want to play a game."""

    player = request.args.get("person")

    play_game = request.args.get("play_game")

    return render_template("greeting.html",
                           person=player,
                           play_game=play_game)
@app.route('/form')
def show_madlib_form():

    answer = request.args.get("play_game")

    if answer == 'yes':
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Display the user's madlib."""

    name = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    beverages = request.args.getlist("beverages")
    beverages = ", ".join(beverages)
    madlib_options = ["madlib.html", "madlib3.html"]

    return render_template(choice(madlib_options),
                           name=name,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           beverages=beverages)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
