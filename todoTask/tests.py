from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task


class TaskAPITests(TestCase):
    def setUp(self):
        # Initializes an API client to make requests
        self.client = APIClient()

        # Creates some test tasks
        self.task_data = {
            "title": "Test Task",
            "description": "This is a test task.",
            "completed": False,
        }
        self.task = Task.objects.create(**self.task_data)

    def test_create_task(self):
        """Test that a task can be created through the API"""
        response = self.client.post("/api/tasks/", self.task_data, format="json")

        # Verifies that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifies that the task was created in the database
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.last().title, self.task_data["title"])

    def test_get_tasks(self):
        """Test that tasks can be fetched through the API"""
        response = self.client.get("/api/tasks/", format="json")

        # Verifies that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifies that the created task is in the response
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.task_data["title"])

    def test_update_task(self):
        """Test that a task can be updated through the API"""
        updated_data = {
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True,
        }
        response = self.client.put(
            f"/api/tasks/{self.task.id}/", updated_data, format="json"
        )

        # Verifies that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifies that the task data was updated
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data["title"])
        self.assertEqual(self.task.description, updated_data["description"])
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        """Test that a task can be deleted through the API"""
        response = self.client.delete(f"/api/tasks/{self.task.id}/", format="json")

        # Verifies that the response status code is 204 (No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verifies that the task was deleted from the database
        self.assertEqual(Task.objects.count(), 0)
