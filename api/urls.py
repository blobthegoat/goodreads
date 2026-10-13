from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'users', views.UserViewSet, basename='customuser')
router.register(r'reviews', views.RatingViewSet, basename='rating')

urlpatterns = [
    path("", include(router.urls)),
]
