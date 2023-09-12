from django.test import TestCase
from main.models import Product

# Create your tests here.

from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        self.product = Product.objects.create(
            name="Sample Product",
            amount=10,
            price=100,
            description="Percobaan test case membuat produk."
        )

    def test_product_creation(self):
        #cek apakah produk sudah terbuat dengan sukses atau bukan 
        self.assertEqual(self.product.name, "Sample Product")
        self.assertEqual(self.product.amount, 10)
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.description, "Percobaan test case membuat produk.")