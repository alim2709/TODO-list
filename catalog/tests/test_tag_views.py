from django.test import TestCase
from django.urls import reverse

from catalog.models import Tag

TAG_LIST_URL = reverse("catalog:tag-list")


class PrivateManufacturerViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for tag_id in range(8):
            Tag.objects.create(
                name=f"Test Name-{tag_id}"
            )

    def test_view_url_exist_at_desired_location(self):
        response = self.client.get("/tags/")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(TAG_LIST_URL)

        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(TAG_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/tag_list.html")
