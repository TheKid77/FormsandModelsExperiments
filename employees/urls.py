from django.urls import path
from .views import HomePageView, add_employee, add_annual_review, HomePageView


urlpatterns = [
    path('add_employee/', add_employee, name='add_employee'),
    path('add_annual_review/', add_annual_review, name='add_annual_review'),
    path('', HomePageView.as_view(), name='home')
]