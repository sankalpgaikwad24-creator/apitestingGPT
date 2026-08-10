def test_users(api_context):

    payload = {
        "name": "Sankalp",
        "username": "QAEngineer",
        "email": "sankalp@test.com"
    }

    response = api_context.post(
        "/users",
        data=payload
    )

    body = response.json()

    print("Code is:", response.status)
    print("Response body:", body)

    assert response.status == 201
    assert body["name"] == "Sankalp"
    assert body["username"] == "QAEngineer"
    assert body["email"] == "sankalp@test.com"
    assert "id" in body
