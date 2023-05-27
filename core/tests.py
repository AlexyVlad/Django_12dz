from django.test import TestCase
from django.urls import reverse
from core.models import Course

class CourseTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            name="Test",
            price="10.00"
        )

    def test_course_list_view(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.name)

    def test_course_detail_view(self):
        response = self.client.get(reverse('course', args=[self.course.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.course.name)
        self.assertContains(response, self.course.price)

    def test_course_add_view(self):
        response = self.client.post(reverse('add_course'), {
            'name': 'New',
            'price': '20.00'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.count(), 2)

    def test_course_delete_view(self):
        response = self.client.post(reverse('delete_course', args=[self.course.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Course.objects.count(), 0)

    def test_course_update_view(self):
        response = self.client.post(reverse('update', args=[self.course.pk]), {
            'name': 'Updated',
            'price': '15.00'
        })
        self.assertEqual(response.status_code, 302)
        self.course.refresh_from_db()
        self.assertEqual(self.course.name, 'Updated Course')
