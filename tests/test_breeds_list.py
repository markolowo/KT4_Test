import pytest

pytestmark = pytest.mark.breeds_list


def test_list_all_returns_success(dog_api):
    response = dog_api.all_breeds()

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_list_all_is_dictionary_of_breeds(all_breeds):
    assert isinstance(all_breeds, dict)
    assert len(all_breeds) > 50


@pytest.mark.parametrize("breed", ["hound", "bulldog", "retriever", "terrier", "pug"])
def test_known_breed_is_in_list(all_breeds, breed):
    assert breed in all_breeds


def test_sub_breeds_are_lists_of_strings(all_breeds):
    for breed, sub_breeds in all_breeds.items():
        assert isinstance(sub_breeds, list), breed
        assert all(isinstance(sub_breed, str) for sub_breed in sub_breeds), breed


def test_breed_names_are_lowercase(all_breeds):
    for breed in all_breeds:
        assert breed == breed.lower()
