import flask
import mongoengine as me
from api_constants import mongo_password, mongo_user
# This extension adds a toolbar overlay to Flask applications containing useful information for debugging. =>
from flask_debugtoolbar import DebugToolbarExtension
from models.model import db, User
from routes.UserRoutes import createUser, getUserList
from routes.auth.login_register import loginUser, token_required
from flask_cors import CORS

app = flask.Flask("micro-blog-app")
CORS(app)


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
    return "<html><body>Micro-Blog</body></html>"


app.add_url_rule("/createUser", view_func=createUser,
                 methods=["GET", "POST"])


@app.route("/getUserList", methods=["GET", "POST"])
@token_required
def getUserList(current_user):
    userList = []
    for user in User.objects().order_by("surname"):
        userList.append(user)
    return flask.jsonify(userList)


app.add_url_rule("/login", view_func=loginUser,
                 methods=["GET", "POST"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
