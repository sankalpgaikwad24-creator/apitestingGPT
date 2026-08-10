def test_delete_post(api_context):

    response = api_context.delete("/posts/1")

    print("Status Code:", response.status)
    print("Response Body:", response.text())

    assert response.status == 200