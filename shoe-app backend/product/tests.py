from django.test import TestCase

from account.models import User
from .models import Product, Store, Producer


class deleteProduct(TestCase):
    def setUp(self):
        # Create a product for testing deletion
        self.product = Product.objects.create(
            name="Test Product",
            price=5.00,
            description="This is a test product"
        )

    def test_product_deletion(self):
        initial_count = Product.objects.count()

        # Delete the product
        self.product.delete()

        # Check that the count of products has decreased by 1
        self.assertEqual(Product.objects.count(), initial_count - 1)

        # Check that the product has been deleted
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(name="Test Product")


class ProductManagement(TestCase):

    def setUp(self):
        self.store = Store.objects.create(name="Test Store")
        self.producer = Producer.objects.create(name="Test Producer")
        self.product = Product.objects.create(name="Test Product", store=self.store,
                                              price=10.00, description="Test Description",
                                              producer=self.producer)

    def test_add_product(self):
        product_count = Product.objects.count()
        new_product = Product.objects.create(name="New Product", store=self.store,
                                             price=15.00, description="New Description",
                                             producer=self.producer)
        self.assertEqual(Product.objects.count(), product_count + 1)
        self.assertEqual(new_product.name, "New Product")
        self.assertEqual(new_product.store, self.store)
        self.assertEqual(new_product.price, 15.00)
        self.assertEqual(new_product.description, "New Description")
        self.assertEqual(new_product.producer, self.producer)

    def test_update_product(self):
        updated_name = "Updated Test Product"
        updated_price = 20.00
        updated_description = "Updated Test Description"
        updated_producer = Producer.objects.create(name="Updated Producer")
        self.product.name = updated_name
        self.product.price = updated_price
        self.product.description = updated_description
        self.product.producer = updated_producer
        self.product.save()
        updated_product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(updated_product.name, updated_name)
        self.assertEqual(updated_product.price, updated_price)
        self.assertEqual(updated_product.description, updated_description)
        self.assertEqual(updated_product.producer, updated_producer)


class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_update_user(self):
        # retrieve the user from the database
        user = User.objects.get(username='testuser')
        # update the user's email
        user.email = 'newemail@example.com'
        user.save()
        # retrieve the updated user from the database
        updated_user = User.objects.get(username='testuser')
        # check that the email was updated
        self.assertEqual(updated_user.email, 'newemail@example.com')

    def test_delete_user(self):
        # retrieve the user from the database
        user = User.objects.get(username='testuser')
        # delete the user
        user.delete()
        # check that the user was deleted
        self.assertFalse(User.objects.filter(username='testuser').exists())
