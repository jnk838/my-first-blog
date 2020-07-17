from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import CV
from blog.models import Post
from django.test.client import Client

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  

        html = response.content.decode('utf8')  
        self.assertIn('<title>Jamie King Blog</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'blog/base.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/base.html')

    def test_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'blog/cv.html')

    def test_uses_cv_new_template(self):
        response = self.client.get('/cv/new/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    def test_only_saves_items_when_necessary_Post(self):
        self.client.get('/')
        self.assertEqual(Post.objects.count(), 0)

    def test_only_saves_items_when_necessary_CV(self):
            self.client.get('/')
            self.assertEqual(CV.objects.count(), 0)

    def test_can_save_a_POST_request_cv_edit(self):
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', 'mypassword')
        c = Client()
        c.login(username=my_admin.username, password='mypassword')

        first_item = CV()
        first_item.title = 'Title 1'
        first_item.text = 'A new list item'
        first_item.author = my_admin
        first_item.save()

        self.assertEqual(CV.objects.count(), 1)
        new_item = CV.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_can_save_a_POST_request_cv_new(self):
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', 'mypassword')
        c = Client()
        c.login(username=my_admin.username, password='mypassword')

        first_item = CV()
        first_item.title = 'Title 1'
        first_item.text = 'The first (ever) list item'
        first_item.location = 'Blah'
        first_item.date = '202020'
        first_item.l1 = '1'
        first_item.l2 = '2'
        first_item.l3 = '3'
        first_item.author = my_admin
        first_item.save()

        self.assertEqual(CV.objects.count(), 1)
        new_item = CV.objects.first()
        self.assertEqual(new_item.text, 'The first (ever) list item')

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):

        my_admin = User.objects.create_superuser('myuser','myemail@test.com','mypassword')
        c = Client()
        c.login(username=my_admin.username, password='mypassword')

        first_item = Post()
        first_item.title = 'Title 1'
        first_item.text = 'The first (ever) list item'
        first_item.author = my_admin
        first_item.save()

        second_item = Post()
        second_item.title = 'Title 2'
        second_item.text = 'Item the second'
        second_item.author = my_admin
        second_item.save()

        saved_items = Post.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

    def test_saving_and_retrieving_items_CV(self):

        my_admin = User.objects.create_superuser('myuser','myemail@test.com','mypassword')
        c = Client()
        c.login(username=my_admin.username, password='mypassword')

        first_item = CV()
        first_item.title = 'Title 1'
        first_item.text = 'The first (ever) list item'
        first_item.author = my_admin
        first_item.save()

        second_item = CV()
        second_item.title = 'Title 2'
        second_item.text = 'Item the second'
        second_item.author = my_admin
        second_item.save()

        saved_items = CV.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

    
    def test_saving_and_retrieving_items_new_CV(self):

        my_admin = User.objects.create_superuser('myuser','myemail@test.com','mypassword')
        c = Client()
        c.login(username=my_admin.username, password='mypassword')

        first_item = CV()
        first_item.title = 'Title 1'
        first_item.text = 'The first (ever) list item'
        first_item.location = 'Blah'
        first_item.date = '202020'
        first_item.l1 = '1'
        first_item.l2 = '2'
        first_item.l3 = '3'
        first_item.author = my_admin
        first_item.save()

        second_item = CV()
        second_item.title = 'Title 2'
        second_item.text = 'Item the second'
        second_item.location = 'Blah'
        second_item.date = '202020'
        second_item.l1 = '1'
        second_item.l2 = '2'
        second_item.l3 = '3'
        second_item.author = my_admin
        second_item.save()

        saved_items = CV.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')