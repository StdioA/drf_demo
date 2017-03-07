from django.test import TestCase
from .models import Data
from rest_framework.test import APIClient


class DataRestAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data_item_url = "/data/{}/"
        self.data_url = "/data/"
        self.data_payload = {
            "content": "test"
        }

    def tearDown(self):
        Data.objects.all().delete()

    def test_create(self):
        res = self.client.get(self.data_url)
        data = res.json()
        self.assertEqual(data, [])

        res = self.client.post(self.data_url, self.data_payload)
        data = res.json()
        self.assertEqual(data["content"], self.data_payload["content"])

        obj = Data.objects.first()
        self.assertEqual(obj.content, self.data_payload["content"])

        res = self.client.get(self.data_url)
        data = res.json()
        self.assertEqual(len(data), 1)

    def test_retrive(self):
        obj = Data(content=self.data_payload["content"])
        obj.save()

        res = self.client.get(self.data_item_url.format(obj.id))
        data = res.json()
        self.assertEqual(data["id"], obj.id)
        self.assertEqual(data["content"], obj.content)

    def test_update(self):
        obj = Data(**self.data_payload)
        obj.save()

        data_url = self.data_item_url.format(obj.id)

        res = self.client.get(data_url)
        data = res.json()
        self.assertEqual(data["id"], obj.id)
        self.assertEqual(data["content"], obj.content)

        payload = {
            "content": "Updated content",
        }
        res = self.client.put(data_url, payload)
        data = res.json()
        self.assertEqual(data["content"], payload["content"])

        updated_data = Data.objects.get(id=obj.id)
        self.assertEqual(updated_data.content, payload["content"])

    def test_delete(self):
        obj = Data(content="")
        obj.save()

        data = self.client.get(self.data_url).json()
        self.assertEqual(len(data), 1)

        url = self.data_item_url.format(obj.id)
        self.client.delete(url)

        data = self.client.get(self.data_url).json()
        self.assertEqual(len(data), 0)
        self.assertEqual(Data.objects.count(), 0)
