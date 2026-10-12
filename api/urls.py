from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'reviews', views.RatingViewSet, basename='review')

urlpatterns = [
    path("", include(router.urls)),
]
