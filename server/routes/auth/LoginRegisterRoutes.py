from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from models.model import User
from Global.JWT_service import token_required
import json
import datetime
import jwt


# ------------------------------------------------------------
# create new user
def createUser():
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
        return json.dumps(out)
# ------------------------------------------------------------

# ------------------------------------------------------------
# user login


def loginUser():
    body_form_data = request.get_json()
    print(body_form_data)
    authUserEmail = body_form_data.get('email')
    authPassword = body_form_data.get('password')
    if not authUserEmail or not authPassword:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    user = User.objects(email=authUserEmail).first()
    if not authUserEmail or not authPassword:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    if check_password_hash(user.password, authPassword):
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, 'micro-blog-playground')

        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
# -----------------------------------------------------------
