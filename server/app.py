'''
1. Create a MongoDB Atlas Database - Done
2. Connect to the database
3. Define an user document collection
4. Create a new book documnet and add it to the collection
5. Fetch the document
6. Update the document
7. Run queries on the collection
8. Delete Document
'''
import flask
import mongoengine as me
from api_constants import mongo_password, mongo_user
# This extension adds a toolbar overlay to Flask applications containing useful information for debugging. =>
from flask_debugtoolbar import DebugToolbarExtension
from models.model import db
from routes.UserRoutes import createUser, getUserList
from flask_cors import CORS

app = flask.Flask("micro-blog-app")
CORS(app)
CORS(app, resources={r"\*": {'origins': "*"}})
CORS(app, resources={r'\*': {'origins': 'http://localhost:8080',
                             "allow_headers": "Access-Control-Allow-Origin", "Content-Type": "application/json", 'Accept': "application/json"}})


# The toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config["TESTING"] = True
app.config['SECRET_KEY'] = 'micro-blog-playground'
DebugToolbarExtension(app)

db.init_app(app)
me.disconnect()
# 2. conneect to the database
database_name = "micro-blog"
user = mongo_user
password = mongo_password
DB_URI = "mongodb+srv://{}:{}@cluster0.ldccoab.mongodb.net/{}?retryWrites=true&w=majority".format(user,
                                                                                                  password, database_name)
me.connect(host=DB_URI)


@app.route("/")
def hello_world():
    return "<p>Micro-Blog</p>"


app.add_url_rule("/createUser", view_func=createUser,
                 methods=["GET", "POST"])

app.add_url_rule("/getUserList", view_func=getUserList,
                 methods=["GET", "POST"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
