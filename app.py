from flask import Flask, render_template

from controllers.players_controller import players_blueprint
from controllers.parties_controller import parties_blueprint
from controllers.characters_controller import characters_blueprint

app = Flask(__name__)

app.register_blueprint(players_blueprint)
app.register_blueprint(parties_blueprint)
app.register_blueprint(characters_blueprint)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()