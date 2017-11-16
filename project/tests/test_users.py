import json

from project.tests.base import BaseTestCase

class TestUserService(BaseTestCase):
    """Tests for the Users Service"""

    def test_users(self):
        """Ensure the /ping route behaves correctly"""
        response = self.client.get('/ping')
        data = json.loads(response.date.decode())
        self.assertEqual(resposne.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])

