from django.conf import settings
import requests
from rest_framework.test import APISimpleTestCase


class HelloWorld(APISimpleTestCase):
    def test_root(self):
        resp = self.client.get("/")
        assert resp.status_code == 200


class CheckLeirecordsUrl(APISimpleTestCase):
    def test_lei_endpoint(self):
        response = requests.get(settings.LEI_LOOKUP_URL)
        error = response.json()
        assert error["status_code"] == 400  # Should be error status with no params
        assert error["message"] == "Query parameter `lei` is missing."


