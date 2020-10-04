from flask import Blueprint, Flask, redirect, render_template, request

import repos.character_repository as character_repository
import repos.party_repository as party_repository
import repos.player_repository as player_repository


# index
# show
# new
# create
# edit
# update
# delete