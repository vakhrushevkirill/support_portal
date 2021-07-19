from django.test import TestCase
from django.core.exceptions import ValidationError
from news.models import News
from users.models import UserPortal
from django.utils import timezone

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Пусть будет что то в БД")
        #print(UserPortal.objects.create_user("User"))
        News.objects.create(
            title = 'sadasdasfdfdsfdsfdsfdsfdf',
            description = 'dsfdsfsdfdsfdsf',
            text = 'models.TextField()',
            create_on = timezone.now(),
            commetns_count = 0,
            author_id = UserPortal.objects.create_user("UserTest")

        )

    def setUp(self):
        print("Запуск теста")
        self.news=News.objects.create(
            title = 'Заголовок',
            description = 'dsfdsfsdfdsfdsf',
            text = 'models.TextField()',
            create_on = timezone.now(),
            commetns_count = 0,
            author_id = UserPortal.objects.create_user("UserTestOther")

        )

    def tearDown(self):
        print('Конец теста')

    def test_create_title(self):
        self.assertEqual(self.news.title, 'Заголовок')

    def test_records(self):
        self.assertEqual(len(News.objects.all()), 2)

    def test_d(self):
        news_lost = None
        with self.assertRaises(ValidationError) as cm:
            news_lost=News.objects.create(
            title = 'Заголовок',
            description = 'dsfdsfsdfdsfdsf',
            text = 'models.TextField()',
            create_on = 'timezone.now()',
            commetns_count = 0,
            author_id = UserPortal.objects.create_user("UserTest2Other")
            )
        
