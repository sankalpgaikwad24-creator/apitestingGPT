def test_get_posts_by_user(api_context):

    response = api_context.get(
        "/posts",
        params={
            "userId": 2
        }
    )

    print("Status Code:", response.status)

    print("Response:", response.json())

    assert response.status == 200

    body = response.json()

    assert len(body) > 0

    for post in body:
        assert post["userId"] == 2