def test_put(api_context):

    payload = {
        "title": "sankalp gaikwad",
        "body": "python tester2",
        "userId": 5
    }

    response = api_context.put(
        "/posts/1",
        data=payload
    )

    print("Status Code:", response.status)

    assert response.status == 200

    body = response.json()

    print("Response Body:", body)

    assert body["id"] == 1
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]