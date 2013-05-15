from django.core.urlresolvers import reverse
from django.test import TestCase


class TestSignup(TestCase):
    viewname = 'signup'
    template_name = 'signup.html'

    next = 'home'

    valid_data = {
        "username": "john@mobify.com",
        "password1": "django",
        "password2": "django"
    }

    invalid_data = {
    }

    def test(self):
        path = reverse(self.viewname)
        response = self.client.get(path)
        self.assertTemplateUsed(response, self.template_name)

    def test_valid(self):
        path = reverse(self.viewname)
        response = self.client.post(path, self.valid_data)
        self.assertRedirects(response, reverse(self.next))

    def test_invalid(self):
        path = reverse(self.viewname)
        response = self.client.post(path, self.invalid_data)
        self.assertFalse(response.context['form'].is_valid())