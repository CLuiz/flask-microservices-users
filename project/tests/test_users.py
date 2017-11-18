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

    def test_add_user(self):
        """Ensure a new user can be added to the database."""
        with self.client:
            response = self.client.post(
                '/users',
                data = json.dumps(dict(
                    username='chris',
                    email='chris@chrisluiz.io'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('chris@chrisluiz.io was added!', data['message'])
            self.asssertIn('success', data['status'])
