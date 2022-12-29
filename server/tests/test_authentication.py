from src.models.user_model import User


def test_login_with_incorrect_password(app_client):
    response = app_client.post(
        "/login", json={"email": "foo@bar.com", "password": "bar"}
    )

    assert response.status_code == 401
    assert response.text == "Could not verify"
