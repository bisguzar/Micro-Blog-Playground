from flask_mongoengine import MongoEngine
from mongoengine import connect

db = MongoEngine()


class StatusCodeEnums:
    stat0 = {"msg": "Success", "code": 200}
    stat1 = {"msg": "Not found", "code": 404}
    stat2 = {"msg": "Invalid Request", "code": 400}
    stat3 = {"msg": "Unauthorized", "code": 401}
    stat4 = {"msg": "Something went wrong", "code": 400}
