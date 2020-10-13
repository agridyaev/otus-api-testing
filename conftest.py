import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com/posts",
        help="Request base url"
    )


@pytest.fixture(scope="module")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def session():
    return requests.Session()
