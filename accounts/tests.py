from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username    = 'Vik',
            email       = 'my@email.local',
            password    = 'pass123',
        )
        self.assertEqual(user.username, 'Vik')
        self.assertEqual(user.email, 'my@email.local')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username    = 'superadmin',
            email       = 'superadmin@email.local',
            password    = 'admin_user',
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.local')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
