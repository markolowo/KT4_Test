import pytest

from conftest import is_image_url

pytestmark = pytest.mark.random_images

MAX_IMAGES_BY_DOCUMENTATION = 50


def test_random_image_returns_one_image_url(dog_api):
    response = dog_api.random_image()

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert is_image_url(response.json()["message"])


@pytest.mark.parametrize("count", [1, 3, 10])
def test_random_images_returns_requested_count(dog_api, count):
    images = dog_api.random_images(count).json()["message"]

    assert len(images) == count
    assert all(is_image_url(image) for image in images)


def test_random_images_maximum_is_50(dog_api):
    images = dog_api.random_images(MAX_IMAGES_BY_DOCUMENTATION).json()["message"]

    assert len(images) == MAX_IMAGES_BY_DOCUMENTATION


@pytest.mark.xfail(strict=True, reason="Дефект DOG-1: сервер возвращает больше 50 картинок, хотя по документации максимум 50")
def test_random_images_over_maximum_is_limited_to_50(dog_api):
    images = dog_api.random_images(51).json()["message"]

    assert len(images) <= MAX_IMAGES_BY_DOCUMENTATION


@pytest.mark.xfail(strict=True, reason="Дефект DOG-2: некорректное количество не отклоняется, возвращается 1 картинка и статус 200")
@pytest.mark.parametrize("count", ["abc", -1, 0])
def test_random_images_invalid_count_is_rejected(dog_api, count):
    response = dog_api.random_images(count)

    assert response.status_code == 400
