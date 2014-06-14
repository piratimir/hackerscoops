from django.contrib.auth.models import User
from django.test import Client, TestCase
from article import models

class CategoryTest(TestCase):

    def test_model_can_be_created(self):

        category = models.Category.objects.create(
            name='Cat 1', description='Category 1 is long')

        self.assertEqual(category.name, 'Cat 1')
        self.assertEqual(category.description, 'Category 1 is long')

    def test_unicode_representation(self):
        category = models.Category.objects.create(
            name='Cat 2', description='Category 2 is long')

        self.assertEqual(unicode(category), 'Cat 2')


class HomeViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='jetbird')
        self.client = Client()

    def test_home_view_returns_response(self):

        response = self.client.get('/')

        self.assertIn('<h1>HackerScoops</h1>', response.content)

    def test_view_context_contains_last_ten_articles(self):
        for ii in range(15):
            models.Article.objects.create(
                title='Art %s' % (ii,),
                author=self.user,
                body=''
            )

        response = self.client.get('/')

        self.assertEqual(len(response.context['articles']), 10)
        self.assertEqual(response.context['articles'][0].title, 'Art 0')
        self.assertEqual(response.context['articles'][9].title, 'Art 9')
