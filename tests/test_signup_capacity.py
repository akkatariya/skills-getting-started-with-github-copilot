from src.app import activities


def test_signup_rejects_when_activity_is_full(client):
    activity_name = "Debate Club"
    max_participants = activities[activity_name]["max_participants"]
    activities[activity_name]["participants"] = [f"student{i}@mergington.edu" for i in range(max_participants)]

    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": "overflow.student@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Activity is already full"}
