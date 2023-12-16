from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Thing


class ThingsCreateUpdateDeleteTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.thing = Thing.objects.create(
            name="pickle", rating=1, reviewer=self.user
        )

    def test_string_representation(self):
        self.assertEqual(str(self.thing), "pickle")

    def test_thing_content(self):
        self.assertEqual(f"{self.thing.name}", "pickle")
        self.assertEqual(f"{self.thing.reviewer}", "tester")
        self.assertEqual(self.thing.rating, 1)

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("thing_create"),
            {
                "name": "Rake",
                "rating": 2,
                "reviewer": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("thing_detail", args="2"))
        self.assertContains(response, "Rake")

    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("thing_update", args="1"),
            {"name": "Updated name", "rating": 3, "reviewer": self.user.id}
        )

        self.assertRedirects(response, reverse("thing_detail", args="1"), target_status_code=200)

    def test_thing_delete_view(self):
        response = self.client.get(reverse("thing_delete", args="1"))
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, reverse("thing_list"), target_status_code=200)


class ThingsReadTests(TestCase):
    def setUp(self):
        reviewer = get_user_model().objects.create(username="tester", password="tester")
        Thing.objects.create(name="rake", reviewer=reviewer)

    def test_list_page_status_code(self):
        url = reverse('thing_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('thing_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'thing_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('thing_list')
        response = self.client.get(url)
        things = response.context['object_list']
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0].name, "rake")
        self.assertEqual(things[0].rating, 0)
        self.assertEqual(things[0].reviewer.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('thing_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('thing_detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'thing_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('thing_detail', args=(1,))
        response = self.client.get(url)
        thing = response.context['thing']
        self.assertEqual(thing.name, "rake")
        self.assertEqual(thing.rating, 0)
        self.assertEqual(thing.reviewer.username, "tester")
