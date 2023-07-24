from django.test import TestCase
from django.urls import reverse

from catalog.models import Tag, Task

TASK_LIST_URL = reverse("catalog:todo-list")


class TaskViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for task_id in range(8):
            Task.objects.create(
                name=f"Test Model-{task_id}",
            )

    def test_view_url_exist_at_desired_location(self):
        response = self.client.get("")

        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(TASK_LIST_URL)

        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(TASK_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/index.html")
