from django.urls import path

from . import views

urlpatterns = [
    path('partners/<int:pk>/', views.PartnerUpdateView.as_view(), name='partners'),
    path('partners/', views.PartnerView.as_view(), name='add_partner'),
    path('', views.IndexView.as_view(), name='index')
]
