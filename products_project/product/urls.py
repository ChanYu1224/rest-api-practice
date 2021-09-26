from rest_framework import routers
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name="detail"),
]

#rest api
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)