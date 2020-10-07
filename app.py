from flask import Flask, Blueprint, flash, render_template

from controllers.players_controller import players_blueprint
from controllers.parties_controller import parties_blueprint
from controllers.characters_controller import characters_blueprint
from repos.party_repository import party_repository

app = Flask(__name__)
app.secret_key="182736459"


app.register_blueprint(players_blueprint)
app.register_blueprint(parties_blueprint)
app.register_blueprint(characters_blueprint)

@app.route("/")
def main():
    parties = party_repository.select_all()
    parties.sort(key=lambda party: party.next_game)
    return render_template('index.html', parties=parties)


if __name__ == '__main__':
    app.run(debug=true)