from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from models.user_model import User
import datetime
import jwt
from bson import json_util
import json

# ------------------------------------------------------------
# create new user
def register():
    # # to save the instance to the mongoDB collection = >

    token = None
    post_data = request.json
    body_form_data = request.get_json()
    user = User.objects(email=body_form_data.get('email')).first()

    if user:
        return make_response('User already exists', 401, {'WWW-Authenticate': 'Basic realm="User Exists"'})
    else:
        hash_hassword = generate_password_hash(
            body_form_data.get('password'), method='sha256')
        user = User(name=body_form_data.get('name'),
                    surname=body_form_data.get('surname'), username=body_form_data.get('username'), password=hash_hassword, email=body_form_data.get('email'))
        user.save()
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, 'micro-blog-playground')
        post_data["token"] = token
        out = {"result": post_data, "status": "success",
               "message": "user created"}
        return make_response(out, 200)
# ------------------------------------------------------------

# ------------------------------------------------------------
# user login


def login():
    body_form_data = request.get_json()
    authUserEmail = body_form_data.get('email')
    authPassword = body_form_data.get('password')


    if not authUserEmail or not authPassword:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    user = User.objects(email=authUserEmail).first()
    response_data = {"uid": user.id}
    if not authUserEmail or not authPassword:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    if check_password_hash(user.password, authPassword):
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(hours=6)}, 'micro-blog-playground')
        response_data["token"] = token

        json_data_with_backslashes = json_util.dumps(response_data)
        json_data = json.loads(json_data_with_backslashes)

        return make_response(json_data, 200)

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
# -----------------------------------------------------------
