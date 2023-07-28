from django.test import TestCase

from catalog.models import Task, Tag


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        Task.objects.create(
            name="test name",
            content="test content",
            deadline="2023-07-24"
        )
        Tag.objects.create(
            name="test",
        )

    def test_task_str(self):
        format_ = Task.objects.get(id=1)

        self.assertEqual(str(format_), f"{format_.name}")

    def test_tag_str(self):
        tag = Tag.objects.get(id=1)

        self.assertEqual(
            str(tag),
            f"{tag.name}"
        )
