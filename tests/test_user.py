import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="test@example.com", name="Test User", password="password")

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)

    def test_email_unique(self):
        users = [self.user]
        new_user = User(email="test2@example.com", name="New User", password="newpassword")
        self.assertTrue(User.is_email_unique(new_user.email, users))
        self.assertFalse(User.is_email_unique(self.user.email, users))

if __name__ == "__main__":
    unittest.main()
