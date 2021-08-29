from django.test import TestCase

# Create your tests here.

from news.models import News
from users.models import UserPortal
from django.utils import timezone
from django.urls import reverse

class NewsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_news = 13
        for news_num in range(number_of_news):
            News.objects.create(
            title = f'Заголовок {news_num}',
            description = 'dsfdsfsdfdsfdsf',
            text = 'models.TextField()',
            create_on = timezone.now(),
            commetns_count = 0,
            author_id = UserPortal.objects.create_user(f"UserTestOther {news_num}")
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/news/')
        print('Статус:', resp.status_code)
        self.assertEqual(resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, 302)

    # def test_view_uses_correct_template(self):
    #     resp = self.client.get('/news/')
    #     self.assertEqual(resp.status_code, 302)
    #     self.assertTemplateUsed(resp, 'news/news_list.html')

    # def test_objects_len(self):
    #     resp = self.client.get('/news/')
    #     self.assertEqual(resp.status_code, 302)
    #     self.assertTrue('object_list' in resp.context)
    #     self.assertIn('object_list', resp.context)
    #     self.assertTrue( len(resp.context['object_list']) == 13)

