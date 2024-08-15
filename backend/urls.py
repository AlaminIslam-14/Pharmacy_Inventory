from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
# Add the App library
#from app import views as app_views
from accounts import views as accounts_views
from drug import views as drug_views

router = DefaultRouter()
# Add the App routes
#router.register(r'app_name', app_views.AppViewSet)
router.register(r'accounts', accounts_views.AccountsViewSet, basename='accounts')
router.register(r'drug', drug_views.DrugViewSet, basename='drug')

urlpatterns = [
    path('api/', include(router.urls)),
]