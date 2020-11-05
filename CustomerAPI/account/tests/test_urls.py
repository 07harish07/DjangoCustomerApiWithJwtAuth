from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.api.views import CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('CustomerListView')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, CustomerListView)

    def test_detail_url_resolves(self):
        url = reverse('CustomerDetailView', args=['1'])
        self.assertEquals(resolve(url).func, CustomerDetailView)

    def test_create_url_resolves(self):
        url = reverse('CustomerCreateView')
        self.assertEquals(resolve(url).func, CustomerCreateView)

    def test_update_url_resolves(self):
        url = reverse('CustomerUpdateView', args=['1'])
        self.assertEquals(resolve(url).func, CustomerUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('CustomerDeleteView', args=['1'])
        self.assertEquals(resolve(url).func, CustomerDeleteView)