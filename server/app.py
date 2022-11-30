# imports
import json
import flask
import mongoengine as me
from api_constants import mongo_password, mongo_user
# This extension adds a toolbar overlay to Flask applications containing useful information for debugging. =>
from flask_debugtoolbar import DebugToolbarExtension
from models.user_model import db
from routes.user_routes import users
from routes.auth.login_register_routes import login, register
from routes.blog_posts_routes import add_post, posts, blog_post_categories
from flask_cors import CORS

with open('config.json', 'r') as f:
    config = json.load(f)


app = flask.Flask(config["APP_NAME"])
CORS(app)


# The toolbar is only enabled in debug mode:
app.debug = config["DEBUG"]

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config["TESTING"] = config["TESTING"]
app.config['SECRET_KEY'] = config["SECRET_KEY"]

DebugToolbarExtension(app)

db.init_app(app)
me.disconnect()
# 2. conneect to the database
database_name = config["DB_NAME"]
user = mongo_user
password = mongo_password
DB_URI = "mongodb+srv://{}:{}@cluster0.ldccoab.mongodb.net/{}?retryWrites=true&w=majority".format(user,
                                                                                                  password, database_name)
me.connect(host=DB_URI)

# ----------------------------------------------------
# * User routes start
app.add_url_rule("/register", view_func=register,
                 methods=["GET", "POST"])

app.add_url_rule("/users", methods=["GET"], view_func=users)

app.add_url_rule("/login", view_func=login,
                 methods=["GET", "POST"])
# ----------------------------------------------------
# ----------------------------------------------------
# * Blog Posts routes start
app.add_url_rule("/blog_posts/add", view_func=add_post,
                 methods=["POST"])

app.add_url_rule("/blog_posts", view_func=posts,
                 methods=["GET"])

app.add_url_rule("/blog_posts/categories", view_func=blog_post_categories,
                 methods=["GET"])

# app.add_url_rule("/blog_posts/add_category", view_func=add_category,
#                  methods=["POST"])

# ----------------------------------------------------


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
