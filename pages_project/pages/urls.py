from django.urls import path
from .views import HomePageView,AboutPage

urlpatterns = [
path('about/', AboutPage.as_view(), name='about'),
path('', HomePageView.as_view(), name='home'),
path('home/', HomePageView.as_view(), name='home'),
]
