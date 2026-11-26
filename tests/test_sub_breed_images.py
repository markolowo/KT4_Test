import pytest

from conftest import is_image_url

pytestmark = pytest.mark.sub_breed_images

BREED = "hound"
SUB_BREED = "afghan"
FOLDER = f"/breeds/{BREED}-{SUB_BREED}/"


def test_sub_breed_images_returns_list_of_photos(dog_api):
    response = dog_api.sub_breed_images(BREED, SUB_BREED)

    assert response.status_code == 200
    images = response.json()["message"]
    assert len(images) > 0
    assert all(is_image_url(image) and FOLDER in image for image in images)


def test_sub_breed_random_image_belongs_to_sub_breed(dog_api):
    image = dog_api.sub_breed_random_image(BREED, SUB_BREED).json()["message"]

    assert is_image_url(image)
    assert FOLDER in image


def test_sub_breed_random_images_returns_requested_count(dog_api):
    images = dog_api.sub_breed_random_images(BREED, SUB_BREED, 3).json()["message"]

    assert len(images) == 3
    assert all(FOLDER in image for image in images)


def test_unknown_sub_breed_returns_404(dog_api):
    response = dog_api.sub_breed_images(BREED, "unknownsub")

    assert response.status_code == 404
    assert response.json()["message"] == "Breed not found (sub breed does not exist)"


def test_sub_breed_of_unknown_breed_returns_404(dog_api):
    response = dog_api.sub_breed_images("unknownbreed", SUB_BREED)

    assert response.status_code == 404
    assert response.json()["status"] == "error"
