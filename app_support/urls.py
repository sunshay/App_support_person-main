from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app_support import views
  
urlpatterns = [
    path('country/', views.CountryList.as_view()),
    path('state/', views.StateList.as_view()),
    path('city/', views.CityList.as_view()),
    path('departement/', views.DepartementList.as_view()),
    path('user/', views.UserList.as_view()),
    path('period/', views.PeriodList.as_view()),
    path('product/', views.ProductList.as_view()),
    path('', views.ReparationList.as_view()),
    path('support_person/<int:pk>/', views.RepartionDetail.as_view()),
]