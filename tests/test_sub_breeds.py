import pytest

pytestmark = pytest.mark.sub_breeds


def test_sub_breeds_list_returns_success(dog_api):
    response = dog_api.sub_breeds("hound")

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_hound_has_expected_sub_breeds(dog_api):
    sub_breeds = dog_api.sub_breeds("hound").json()["message"]

    assert {"afghan", "basset", "english"} <= set(sub_breeds)


def test_breed_without_sub_breeds_returns_empty_list(dog_api):
    sub_breeds = dog_api.sub_breeds("pug").json()["message"]

    assert sub_breeds == []


@pytest.mark.parametrize("breed", ["hound", "terrier", "bulldog"])
def test_sub_breeds_match_list_all(dog_api, all_breeds, breed):
    sub_breeds = dog_api.sub_breeds(breed).json()["message"]

    assert sorted(sub_breeds) == sorted(all_breeds[breed])


def test_unknown_breed_sub_breeds_returns_404(dog_api):
    response = dog_api.sub_breeds("unknownbreed")

    assert response.status_code == 404
    assert response.json()["status"] == "error"
