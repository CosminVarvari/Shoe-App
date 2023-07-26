# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from account.views import login_request, logout_view, register, manager_register, employee_register, admin_register


class AccountUrlsTests(SimpleTestCase):

    def test_get_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_request)

    def test_get_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_get_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_get_manager_register(self):
        url = reverse('manager_register')
        self.assertEquals(resolve(url).func.view_class, manager_register)

    def test_get_employee_register(self):
        url = reverse('employee_register')
        self.assertEquals(resolve(url).func.view_class, employee_register)

    def test_get_admin_register(self):
        url = reverse('admin_register')
        self.assertEquals(resolve(url).func.view_class, admin_register)

