import unittest
from xml.dom import ValidationErr

from mongoengine import connect, disconnect, Document, StringField
from werkzeug.security import generate_password_hash
from parameterized import parameterized


class User(Document):
    """
    User model for user collection
    user_id
    name
    surname
    """
    name = StringField(null=False, required=True, exists=True)
    surname = StringField(null=False, required=True, exists=True)
    username = StringField(null=False, required=True, exists=True)
    email = StringField(null=False, required=True, exists=True)
    us_password = StringField(null=False, required=True, exists=True)


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost', uuidRepresentation="standard", port=27017, alias='default'
                )

    @classmethod
    def tearDownClass(cls):
        disconnect()

    # @parameterized.expand([
    #     ["Abcde12345", True],
    #     ["sadsas1", True],
    #     ["Abcdess12345", False],
    #     ["12345", False]
    # ])
    # def test_validate_password(self, password, valid):
    #     # given

    #     data = {
    #         "name": "Arda",
    #         "surname": "Bozlak",
    #         "username": "ardabzlk",
    #         "email": "ardabzlk@gmail.com",
    #         "password": password
    #     }
    #     # when
    #     try:
    #         user = User(name=data['name'],
    #                     surname=data['surname'], username=data['username'], us_password=password, email=data['email'])
    #         user.save()
    #         assert valid
    #         # then
    #         assert user is not None
    #         assert user.name == data["name"]
    #         assert user.surname == data["surname"]
    #         assert user.username == data["username"]
    #         assert user.email == data["email"]
    #         assert user.us_password == password
    #     except ValidationErr:
    #         assert not valid

    @classmethod
    def test_missing_fields(self):
        # given
        data = {
            "name": "Arda",
            "surname": "Bozlak",
            "username": "ardabzlk",
            "password": "Abcde12345"
        }

        user = User(name=data['name'],
                    surname=data['surname'], username=data['username'], us_password=data['password'], email=data['email'])
        # when / then

        with self.assertRaises(ValidationErr("Missing fields")):
            print("exc")


if __name__ == '__main__':
    unittest.main()
