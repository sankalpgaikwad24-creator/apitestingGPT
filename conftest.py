import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_context():

    with sync_playwright() as p:

        request = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com"
        )

        yield request

        request.dispose()