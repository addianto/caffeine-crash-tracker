from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry


class MainUnitTest(TestCase):
    def test_main_url_exists(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_main_uses_main_template(self):
        response = Client().get("/")
        self.assertTemplateUsed(response, "main.html")

    def test_nonexistent_page_should_404(self):
        response = Client().get("/skibidi/")
        self.assertEqual(response.status_code, 404)

    def test_happy_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
            mood="Happy",
            time=now,
            feelings="Happy happy happy happy happy",
            mood_intensity=8,
            sadness_level=2,
        )
        self.assertTrue(mood.is_happy)

    def test_main_template_uses_correct_page_title(self):
        response = Client().get("/")
        html_response = response.content.decode("utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)
