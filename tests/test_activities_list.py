def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    chess = payload["Chess Club"]
    assert expected_fields.issubset(chess.keys())
    assert isinstance(chess["participants"], list)


def test_get_activities_includes_seed_data(client):
    # Arrange
    activity_name = "Programming Class"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert activity_name in payload
    assert "emma@mergington.edu" in payload[activity_name]["participants"]
