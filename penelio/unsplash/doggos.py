import re
from unsplash.api import Api
from unsplash.auth import Auth

client_id = "0620ff55bf40eb64492a9b42a556257564b1a0e125192a446da68c0f6286a0c5"
client_secret = "40d5ac32874084a4742ea663d2a309a18ebbdb7448159757a537a6e17dd44ec7"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)
################################################


def search_photos(query):
	data = str(api.photo.random(query=query))
	splitted = re.split(r"[\W']+", data)
	if splitted[3] == '':
		return "EMPTY"
	return splitted[3]
