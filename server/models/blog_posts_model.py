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
    title = db.StringField()
    content = db.StringField()
    date = db.DateField()
    category_id = db.IntField()


class blog_categories(db.Document):

    category_id = db.IntField()
    category_name = db.StringField()
