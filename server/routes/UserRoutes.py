import datetime
from bson import ObjectId
from flask import json, jsonify, request
import jwt
from models import model
from werkzeug.security import generate_password_hash
from routes.auth.login_register import token_required


# create new user


def createUser():
    # # to save the instance to the mongoDB collection = >
    token = None
    post_data = request.json
    body_form_data = request.get_json()
    hash_hassword = generate_password_hash(
        body_form_data.get('password'), method='sha256')
    user = model.User(name=body_form_data.get('name'),
                      surname=body_form_data.get('surname'), username=body_form_data.get('username'), password=hash_hassword, email=body_form_data.get('email'))
    user.save()
    token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow(
    ) + datetime.timedelta(minutes=30)}, 'micro-blog-playground')
    post_data["token"] = token
    out = {"result": post_data, "status": "success",
           "message": "user created"}
    return json.dumps(out)

# get all user list


def getUserList():
    userList = []
    for user in model.User.objects().order_by("surname"):
        userList.append(user)
    return jsonify(userList)


"""

# 3. Define an user document collection

# Name of the collection by defult the class


# create a user

# user = User(user_id=ObjectId(), name="Salih", surname="Bozlak")
# to save the instance to the mongoDB collection =>
# user.save()


# fetch the user
# user = User.objects(name="Ayşe").first()

# update the user
# user.update(id=rndId)

# # add another user
# user = User(user_id=2, name="Meltem", surname="Bozlak")
# user.save()


# userList = []
# for user in User.objects():
#     userList.append(user.to_json())

# print(userList)
# print(userList)

# fetch all the users
# ----------------------------------------------------
# find users whose  surname-name contains Bozlak
# userList = []
# for user in User.objects(surname__contains="Bozlak"):
#     userList.append(user.to_json())
# print(userList)
# ----------------------------------------------------

# ----------------------------------------------------
# how many user are in the collection
# print(User.objects.count())

# order by name field
# userList = []
# for user in User.objects().order_by("surname"):
#     userList.append(user.to_json())
# print(userList)
# ----------------------------------------------------

# ----------------------------------------------------
# delete a user
# user = User.objects(user_id="63778bf2cc442201ca21a45a").first()

# user.delete()

# print(User.objects.count())
# ----------------------------------------------------

# ----------------------------------------------------
# delete all users
# for user in User.objects():
#     user.delete()
# print(User.objects.count())
# ----------------------------------------------------
"""
