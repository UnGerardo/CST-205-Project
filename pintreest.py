#Authors: April Miller
#CST205 Professor Avner
#5 May 2021
#Program description:

#Imports
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request

# import json
# import requests

from unsplash.api import Api
from unsplash.auth import Auth
from unsplash.client import Client
from unsplash.models import Photo as PhotoModel 

#TO DO:
# build page layout (DONE BY APRIL 05/04/2021)
#LINK API - (DONE BY APRIL 05/04/2021) 
#DISPLAY IM0AGES - Gerardo (DONE BY APRIL 05/04/2021)
#Detail page - (currently working)
#Display stars properly -  (Done By Pradeep 05/12/21)
#Add functionality to move through pages 
#Add Reviews
#star rating system (user can click stars to fill in) 

#Client access key, secret access key, redirect uri, and code needed for Unsplashed API.
client_id = "etLgSfNf4HL1N-Gdo2nuNs3UPEtQRGcjOSRYdeFW4uc"
client_secret = "NkBawmzANKngdmS1BwVP25R2MzkVoWVIlM1zD8MjXQw"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = "" 

#Initialize the flask app and activate bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

#URL to website
url = "https://unsplash.com/collections/3334461/national-parks"

#Authorize your API usage.
auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)

#Get the ID of the collection
collection_id = "3334461"
#Get the collection
col = api.collection.photos(collection_id, 1, 277)

#Renders the html and css files
@app.route('/', methods=["GET"])
def home():
    return render_template("index.html", col=col)