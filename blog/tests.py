from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Cat


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.cat = Cat.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_cat_model(self):
        self.assertEqual(self.cat.title, "A good title")
        self.assertEqual(self.cat.body, "Nice body content")
        self.assertEqual(self.cat.author.username, "testuser")
        self.assertEqual(str(self.cat), "A good title")
        self.assertEqual(self.cat.get_absolute_url(), "/cat/1/")

    def test_url_exists_at_correct_location_listview(self):  # 	new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):  # 	new
        response = self.client.get("/cat/1/")
        self.assertEqual(response.status_code, 200)

    def test_cat_listview(self):  # 	new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")

    def test_cat_detailview(self):  # 	new
        response = self.client.get(reverse("cat_detail", kwargs={"pk": self.cat.pk}))
        no_response = self.client.get("/cat/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "cat_detail.html")
