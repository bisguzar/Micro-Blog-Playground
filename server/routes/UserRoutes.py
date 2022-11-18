from bson import ObjectId
from flask import json, jsonify, render_template, request
from models import model

# create new user


def createUser():
    # # to save the instance to the mongoDB collection = >
    post_data = request.json
    body_form_data = request.get_json()
    user = model.User(user_id=ObjectId(), name=body_form_data.get('name'),
                      surname=body_form_data.get('surname'))
    user.save()
    out = {"result": str(post_data)}
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

# fetch all the books
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
