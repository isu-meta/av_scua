from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    '''
        Passes if home template is used at startup
    '''
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'basic/home.html')
