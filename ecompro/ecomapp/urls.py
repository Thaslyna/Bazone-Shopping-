from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allprodcat, name="AllProdCat"),
    path('<slug:c_slug>/', views.allprodcat, name="product_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name="product_details")
]