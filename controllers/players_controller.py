from flask import Blueprint, Flask, redirect, render_template, request

import repos.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

# index
# show
# new
# create
# edit
# update
# delete