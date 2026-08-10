#"PUT is generally used to replace or update the complete resource,
# whereas PATCH is used for a partial update where only the fields that need to
# change are sent."
#from urllib3.contrib.emscripten import response


def test_patch(api_context):

    payload = {
        "title": "Updated title of Playwright"
    }

    response = api_context.patch(
        "/posts/1",
        data=payload
    )

    print("Status Code:", response.status)

    assert response.status == 200

    body = response.json()

    print("Response Body:", body)

    assert body["title"] == "Updated title of Playwright"