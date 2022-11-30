from flask_mongoengine import MongoEngine

db = MongoEngine()


# ----------------------------------------------
# User collection
class blog_posts(db.Document):
    """
    Blog_Posts model for blog_posts collection
    user
    header
    content
    date
    """
    user_id = db.ObjectIdField()
    header = db.StringField()
    content = db.StringField()
    date = db.DateField()
