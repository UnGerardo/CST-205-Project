# COURSE: CST-205
# TITLE: Pinetreest
# ABSTRACT: This program diplays pictures of nature using the Unsplash API. The images are displayed along with their description and you have the ability
# to rate the pictures out of 5 and you can comment in the comment section at the bottom.
# Authors: April Miller, Melody Neely, Pradeep Pansare, and Gerardo Lopez
# Date: 5/17/21

# April built the foundation of the website, in the python file with flask and set up the HTML
# Gerardo added the use of flexbox to the images, in CSS
# Pradeep finished the star rating system, in HTML and CSS
# Melody implemented the star rating on all the images, in HTML and CSS
# Gerardo fixed a bug that dealt with the star rating system, in HTML
# April restyled the page, in HTML and CSS
# Melody added a comment system, worked with flask_wtf and created Comments class and created new HTML file comment.html and added CSS

# GITHUB: https://github.com/UnGerardo/CST-205-Project

#Imports
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect

# import json
# import requests

from unsplash.api import Api
from unsplash.auth import Auth

#wtform imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests,json

#Client access key, secret access key, redirect uri, and code needed for Unsplashed API.
client_id = "etLgSfNf4HL1N-Gdo2nuNs3UPEtQRGcjOSRYdeFW4uc"
client_secret = "NkBawmzANKngdmS1BwVP25R2MzkVoWVIlM1zD8MjXQw"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = "" 

#Initialize the flask app and activate bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
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

#gets comments
class Comments(FlaskForm):
    my_comment= StringField( 
        "Tell Us what you think!",
        validators=[DataRequired()]
    )

comments = []

def store_comments(my_comment):
    comments.append(dict(
        comment= my_comment
    ))

#Renders the html and css files
@app.route('/', methods=('GET','POST'))
def home():
    form = Comments()
    if form.validate_on_submit():
        store_comments(form.my_comment.data)
        print(comments)
        return redirect('/view_comments')
    return render_template("index.html", col=col, form = form)

@app.route('/view_comments')
def vp():
    return render_template('comment.html', comments = comments)


