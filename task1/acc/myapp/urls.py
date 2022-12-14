from django.urls import path
from . import views

urlpatterns = [
    path('',views.SupplierInfoViewSet.as_view()),
    path('shopdetail/',views.ShopDetailViewSet.as_view()),

]