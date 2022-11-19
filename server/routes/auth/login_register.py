# create new user
from flask import jsonify, request, make_response
import jwt
import datetime
from models.model import User
from werkzeug.security import check_password_hash
from functools import wraps


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


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, 'micro-blog-playground',
                              algorithms=['HS256'])
            current_user = User.objects(username=data.get('username')).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated
