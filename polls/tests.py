from django.test import Client
from django.urls import reverse

# Create your tests here.

client = Client()


def test_404_page():
    response = client.get("/polls/404")

    assert response.status_code == 404
