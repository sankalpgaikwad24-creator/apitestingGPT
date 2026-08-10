def test_create_post(api_context):

    payload = {
        "title": "sankalp",
        "body": "python tester",
        "userId": 1
    }

    response = api_context.post(
        "/posts",
        data=payload
    )

    print("Status Code:", response.status)
    print("Response Body:", response.json())

    assert response.status == 201

    body = response.json()

    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body