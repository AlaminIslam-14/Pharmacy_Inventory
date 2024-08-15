from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
# Add the App library
#from app import views as app_views
from accounts import views as accounts_views
from drug import views as drug_views
from stock import views as stock_views

router = DefaultRouter()
# Add the App routes
#router.register(r'app_name', app_views.AppViewSet)
router.register(r'accounts', accounts_views.AccountsViewSet, basename='accounts')
router.register(r'drug', drug_views.DrugViewSet, basename='drug')
router.register(r'stock', stock_views.StockViewSet, basename='stock')

urlpatterns = [
    path('api/', include(router.urls)),
]