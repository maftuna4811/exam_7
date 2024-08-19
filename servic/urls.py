from django.contrib import admin
from django.urls import path, include
from .views import ServicesView, FAQView, BlogView, OfferView, Error404View, AboutView, AdvisersView, FeaturesView, TeamView


urlpatterns = [
    path('advisers/', AdvisersView.as_view(), name='advisers'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('error404/', Error404View.as_view(), name='error404'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('offer/', OfferView.as_view(), name='offer'),
    path('features/', FeaturesView.as_view(), name='features'),
    path('team/', TeamView.as_view, name='team'),
]