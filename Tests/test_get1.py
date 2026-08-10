def test_get_single_post(api_context):

    response = api_context.get("/posts/1")

    assert response.status == 200

    body = response.json()
    print("Status Code:", response.status)

    print("Response Body:", response.text())

    print(body)

    assert body["id"] == 1
    assert body["userId"] == 1
    assert body["title"] != ""