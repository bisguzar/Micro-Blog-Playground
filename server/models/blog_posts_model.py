from models.models import db
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
    user_id = db.ObjectIdField(null=False, required=True, exists=True)
    title = db.StringField(null=False, required=True, exists=True)
    content = db.StringField(null=False, required=True, exists=True)
    date = db.DateField(null=False, required=True, exists=True)
    category_id = db.IntField(null=False, required=True, exists=True)


class blog_categories(db.Document):

    category_id = db.IntField(null=False, required=True, exists=True)
    category_name = db.StringField(null=False, required=True, exists=True)
