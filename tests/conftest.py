import pytest

from api.dog_api import DogApi

IMAGE_HOST = "https://images.dog.ceo/breeds/"


def is_image_url(url):
    return isinstance(url, str) and url.startswith(IMAGE_HOST) and url.lower().endswith((".jpg", ".jpeg", ".png"))


@pytest.fixture(scope="session")
def dog_api():
    return DogApi()


@pytest.fixture(scope="session")
def all_breeds(dog_api):
    return dog_api.all_breeds().json()["message"]
