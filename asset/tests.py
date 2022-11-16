from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from PIL import Image
import tempfile


class AssetTests(APITestCase):

    def test_upload_file(self):
        image = Image.new(mode='RGB', size=(200, 20), color='blue')
        url = reverse('asset_urls:assets-list')

        tmp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(tmp_file)
        tmp_file.seek(0)

        body = {
            'file_high': tmp_file,
        }

        response = self.client.post(url, body, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_created_spot(self):

        url = reverse('asset_urls:spot-list')

        body = {
            'description': 'spot teste',
            'location': 'principal'
        }

        response = self.client.post(url, body, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
