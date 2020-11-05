from django.test import TestCase, Client
from django.urls import reverse
from account.models import Customer
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('CustomerListView')
        self.detail_url = reverse('CustomerDetailView', args=['1'])
        self.create_url = reverse('CustomerCreateView')
        self.update_url = reverse('CustomerUpdateView', args=['1'])
        self.delete_url = reverse('CustomerDeleteView', args=['1'])
        
    def test_customer_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)

    def test_customer_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)

    def test_customer_create_POST(self):

        response = self.client.post(self.create_url, {
            'fname':'cust13',
            'lname':'test12',
            'email':'cust12@test.com',
            'gender':'1'
        })

        self.assertEquals(response.status_code, 201)

    def test_customer_update_PUT(self):

        response = self.client.put(self.update_url, {
            'fname':'cust12',
            'lname':'test12',
            'email':'cust12@test.com',
            'gender':'1'
        })

        self.assertEquals(response.status_code, 200)

    def test_customer_delete_DELETE(self):

        response = self.client.delete(self.delete_url)

        self.assertEquals(response.status_code, 200)

