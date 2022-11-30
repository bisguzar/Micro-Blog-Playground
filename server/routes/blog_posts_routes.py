from flask import request, make_response
from models.blog_posts_model import blog_posts, blog_categories
import datetime
from services.Exceptions import InvalidUsage
from services.JWT_service import token_required
# ------------------------------------------------------------
# create new post


@token_required
def add_post(current_user):
    # user
    # header
    # content
    # date
    # # to save the instance to the mongoDB collection = >
    try:
        body_form_data = request.get_json()
        print(body_form_data)

        blog_post = blog_posts(user_id=body_form_data.get(
            'user_id'), title=body_form_data.get('title'), content=body_form_data.get('content'), category_id=body_form_data.get('category_id'), date=datetime.datetime.today())

        blog_post.save()
        return make_response("success ", 200)
    except:
        raise InvalidUsage('This view is gone', status_code=410)


def add_category():
    # user
    # header
    # content
    # date
    # # to save the instance to the mongoDB collection = >
    try:
        body_form_data = request.get_json()
        print(body_form_data)

        blog_dost = blog_categories(category_id=body_form_data.get(
            'category_id'), category_name=body_form_data.get('category_name'))
        print(blog_dost)
        blog_dost.save()
        return make_response("success ", 200)
    except:
        raise InvalidUsage('This view is gone', status_code=410)

# ------------------------------------------------------------

# ------------------------------------------------------------
# get all posts


@token_required
def posts(current_user):
    posts = []
    for post in blog_posts.objects():
        posts.append(post)
    return make_response(posts)
# ------------------------------------------------------------
# get blog categories


@token_required
def blog_post_categories(current_user):
    post_categories = []
    for category in blog_categories.objects():
        post_categories.append(category)
    return make_response(post_categories)
# ------------------------------------------------------------
