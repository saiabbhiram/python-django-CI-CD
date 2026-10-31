from django.test import TestCase, Client
from django.urls import reverse
from .models import Item


class HealthCheckTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health_check_status_code(self):
        """Test health check returns HTTP 200 OK."""
        response = self.client.get(reverse('health_check'))
        self.assertEqual(response.status_code, 200)

    def test_health_check_payload(self):
        """Test health check returns expected JSON response."""
        response = self.client.get(reverse('health_check'))
        data = response.json()
        self.assertEqual(data.get('status'), 'ok')
        self.assertEqual(data.get('service'), 'django-jenkins-demo')
        self.assertTrue(data.get('database_connected'))


class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_loads(self):
        """Test that index page loads with 200 OK and expected content."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django & Jenkins Freestyle CI Demo')


class ItemModelTests(TestCase):
    def test_create_item(self):
        """Test Item creation and string representation."""
        item = Item.objects.create(
            title='Configure Jenkins Freestyle Project',
            description='Setup build steps, run migrations, and publish JUnit test results.'
        )
        self.assertEqual(str(item), 'Configure Jenkins Freestyle Project')
        self.assertFalse(item.is_completed)

    def test_item_completion_toggle(self):
        """Test updating completion status."""
        item = Item.objects.create(title='Run CI Build')
        item.is_completed = True
        item.save()
        self.assertTrue(Item.objects.get(id=item.id).is_completed)
