# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import ShowAllProductsManager, ShowAllProductsEmployee, ShowAllUsers, addProduct, \
    searchBar


class ProductUrlsTests(SimpleTestCase):

    def test_get_manager_page(self):
        url = reverse('showProductsMng')
        self.assertEquals(resolve(url).func, ShowAllProductsManager)

    def test_get_employee_page(self):
        url = reverse('showProductsEmp')
        self.assertEquals(resolve(url).func, ShowAllProductsEmployee)

    def test_get_admin_page(self):
        url = reverse('adminPage')
        self.assertEquals(resolve(url).func, ShowAllUsers)

    def test_get_add_product(self):
        url = reverse('addProduct')
        self.assertEquals(resolve(url).func, addProduct)

    def test_get_search(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, searchBar)





