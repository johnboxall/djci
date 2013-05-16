from django.core.urlresolvers import reverse
from django.test import TestCase

from selenium.webdriver.chrome.webdriver import WebDriver


class SeleniumMixin(object):
    live_server_url = 'http://localhost:8081'

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumMixin, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumMixin, cls).tearDownClass()

    def get_url(self, viewname, *args, **kwargs):
        path = reverse(viewname, *args, **kwargs)
        return '%s%s' % (self.live_server_url, path)


class SeleniumTestCase(SeleniumMixin, TestCase):
    pass


class TestSignup(SeleniumTestCase):
    def test(self):
        url = self.get_url('signup')

        self.selenium.get(url)

        inputs = {
            "username": "john@mobify.com",
            "password1": "django",
            "password2": "django"
        }

        for name, value in inputs.items():
            element = self.selenium.find_element_by_name(name)
            element.send_keys(value)

        element = self.selenium.find_element_by_name("next")
        element.click()

        # import pdb;pdb.set_trace()