from src.app import activities


def test_signup_for_activity_succeeds_and_adds_participant(client):
    email = "new.student@mergington.edu"
    activity_name = "Basketball Team"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in activities[activity_name]["participants"]


def test_signup_accepts_query_param_contract(client):
    email = "query.param@mergington.edu"
    activity_name = "Art Club"

    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )

    assert response.status_code == 200
    assert email in activities[activity_name]["participants"]
