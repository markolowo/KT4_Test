import pytest

from conftest import is_image_url

pytestmark = pytest.mark.breed_images

BREED = "hound"


def test_breed_images_returns_list_of_breed_photos(dog_api):
    response = dog_api.breed_images(BREED)

    assert response.status_code == 200
    images = response.json()["message"]
    assert len(images) > 0
    assert all(is_image_url(image) and f"/breeds/{BREED}" in image for image in images)


def test_breed_random_image_belongs_to_breed(dog_api):
    image = dog_api.breed_random_image(BREED).json()["message"]

    assert is_image_url(image)
    assert f"/breeds/{BREED}" in image


def test_breed_random_images_returns_requested_count(dog_api):
    images = dog_api.breed_random_images(BREED, 3).json()["message"]

    assert len(images) == 3
    assert all(f"/breeds/{BREED}" in image for image in images)


def test_unknown_breed_returns_404(dog_api):
    response = dog_api.breed_images("unknownbreed")

    assert response.status_code == 404
    assert response.json()["status"] == "error"
    assert response.json()["message"] == "Breed not found (main breed does not exist)"


def test_breed_name_is_case_insensitive(dog_api):
    response = dog_api.breed_random_image(BREED.upper())

    assert response.status_code == 200
    assert f"/breeds/{BREED}" in response.json()["message"]
