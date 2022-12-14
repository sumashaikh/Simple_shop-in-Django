from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name="shopHome"),
    path('about/', views.about , name="AboutUs"),
    path('contact/', views.contact , name="ContactUs"),
    path('tracker/', views.tracker , name="TrackerUs"),
    path('search/', views.search , name="SearchUs"),
    path('productView/', views.productView , name="TrackingStatus"),
    path('checkout/', views.checkout , name="Checkout")

]