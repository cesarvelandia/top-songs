from flask import render_template, jsonify
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

from app import app, topSongsDAO


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/topsongs/api/v1.0/songs', methods=['GET'])
def get_top_songs():
    return jsonify({'songs': topSongsDAO.get_songs()})


@app.route('/topsongs/api/v1.0/songs/year/<year>', methods=['GET'])
def get_top_songs_by_year(year):
    return jsonify({'songs': topSongsDAO.get_songs_by_year(year)})


@app.route('/topsongs/api/v1.0/songs/artist/<artist>', methods=['GET'])
def get_top_songs_by_artist(artist):
    return jsonify({'songs': topSongsDAO.get_songs_by_artist(artist)})
