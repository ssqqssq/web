from django.test import TestCase
from django.contrib.auth.models import User
from .models import Articles
from django.utils import timezone

class ArticlesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаем пользователя для теста
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

        # Создаем объект Articles для теста
        test_article = Articles.objects.create(
            title_talk='Тестовое обращение',
            full_text='Текст тестового обращения',
            owner=test_user
        )
        test_article.save()

    def test_title_talk_label(self):
        article = Articles.objects.get(id=1)
        field_label = article._meta.get_field('title_talk').verbose_name
        self.assertEquals(field_label, 'Тема обращения')

    def test_full_text_label(self):
        article = Articles.objects.get(id=1)
        field_label = article._meta.get_field('full_text').verbose_name
        self.assertEquals(field_label, 'Обращение')

    def test_date_auto_now_add(self):
        article = Articles.objects.get(id=1)
        self.assertTrue(article.date <= timezone.now())

    def test_object_name_is_title_talk(self):
        article = Articles.objects.get(id=1)
        expected_object_name = f'{article.title_talk}'
        self.assertEquals(expected_object_name, str(article))

    def test_get_absolute_url(self):  # Если у вас есть метод get_absolute_url в модели
        article = Articles.objects.get(id=1)
        # Это предполагает, что у вас есть маршрут с именем 'article_detail' и он принимает ID статьи
        self.assertEquals(article.get_absolute_url(), '/articles/1/')
