from django.urls import path
from . import views
from .views import LogoutAPIView

urlpatterns = [
	path('register/', views.registration, name='register'),
	path('logout/', LogoutAPIView.as_view(), name='logout'),
    # ------------------Customer API Urls-----------------------
	path('users/list/', views.UserListView, name="UserListView"),
	path('customers/list/', views.CustomerListView, name="CustomerListView"),
	path('customer/detail/<str:id>', views.CustomerDetailView, name="CustomerDetailView"),
	path('customer/create/', views.CustomerCreateView, name="CustomerCreateView"),
	path('customer/update/<str:id>', views.CustomerUpdateView, name="CustomerUpdateView"),
	path('customer/delete/<str:id>', views.CustomerDeleteView, name="CustomerDeleteView"),
	
]