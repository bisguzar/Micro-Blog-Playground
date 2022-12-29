import pytest

from flask import current_app
import mongomock
from mongoengine import connect, get_connection


@pytest.fixture
def app():
    app = current_app()
    app.config.update({
        "TESTING": True,
    })

    connect('mongoenginetest', host='mongomock://localhost', alias='testdb')

    conn = get_connection('testdb')
    yield app
