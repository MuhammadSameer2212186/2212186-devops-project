def test_create_student(client):
    response = client.post("/students", json={"reg_no": "2212186", "name": "Sameer", "email": "s@test.com"})
    assert response.status_code == 200
    assert response.json()["reg_no"] == "2212186"


def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
