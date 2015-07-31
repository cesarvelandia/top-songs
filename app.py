from flask import Flask, render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps



#TODO: Move connection details
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DATABASE = 'songstohear'
GUARDIAN_COLLECTION =  'guardiantop'
PROJECTION = {'title' : True, 'theme' : True, 'year' : True, 'artist' : True, 'spotify_url.url' : True, '_id': False}

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/guardian/topsongs')
def guardian_topsongs():
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT);
	top_songs_collection = connection[DATABASE][GUARDIAN_COLLECTION];
	top_songs = top_songs_collection.find(projection=PROJECTION)

	json_top_songs = []
	for song in top_songs:
		json_top_songs.append(song)

	json_top_songs = json.dumps(json_top_songs, default=json_util.default)	

	connection.close()
	return json_top_songs;

if __name__ == '__main__':
    app.run()
    