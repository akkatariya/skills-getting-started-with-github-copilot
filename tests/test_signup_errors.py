def test_signup_rejects_unknown_activity(client):
    response = client.post("/activities/Unknown Club/signup", params={"email": "student@mergington.edu"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_rejects_duplicate_participant(client):
    response = client.post("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})

    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up for this activity"}


def test_signup_requires_email_query_param(client):
    response = client.post("/activities/Chess Club/signup")

    assert response.status_code == 422
    detail = response.json()["detail"]
    assert any(error["loc"] == ["query", "email"] for error in detail)
