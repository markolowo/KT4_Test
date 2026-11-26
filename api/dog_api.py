import requests

BASE_URL_DOG_API = "https://dog.ceo/api"


class DogApi:
    def __init__(self, base_url=BASE_URL_DOG_API):
        self.base_url = base_url

    def _get(self, path):
        return requests.get(f"{self.base_url}/{path}", timeout=15)

    def all_breeds(self):
        return self._get("breeds/list/all")

    def random_image(self):
        return self._get("breeds/image/random")

    def random_images(self, count):
        return self._get(f"breeds/image/random/{count}")

    def breed_images(self, breed):
        return self._get(f"breed/{breed}/images")

    def breed_random_image(self, breed):
        return self._get(f"breed/{breed}/images/random")

    def breed_random_images(self, breed, count):
        return self._get(f"breed/{breed}/images/random/{count}")

    def sub_breeds(self, breed):
        return self._get(f"breed/{breed}/list")

    def sub_breed_images(self, breed, sub_breed):
        return self._get(f"breed/{breed}/{sub_breed}/images")

    def sub_breed_random_image(self, breed, sub_breed):
        return self._get(f"breed/{breed}/{sub_breed}/images/random")

    def sub_breed_random_images(self, breed, sub_breed, count):
        return self._get(f"breed/{breed}/{sub_breed}/images/random/{count}")
