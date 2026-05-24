from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="new post",
            body="body content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "new post")
        self.assertEqual(self.post.body, "body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
        self.assertEqual(str(self.post), "new post")
        
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "body content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "body content")
        self.assertTemplateUsed(response, "post_detail.html")
        
        # Testing the 404 case for a post that doesn't exist
        no_response = self.client.get("/post/100000/")
        self.assertEqual(no_response.status_code, 404)

    # --- New CRUD Operation Tests ---

    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"), 
            {
                "title": "New title", 
                "body": "New text", 
                "author": self.user.id,
            }
        )
        # Checking for HTTP 302 Redirect (Django redirects you after successfully creating a post)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args=[self.post.pk]), 
            {
                "title": "Updated title",
                "body": "Updated text",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)