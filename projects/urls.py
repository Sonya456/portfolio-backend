from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, ProjectViewSet, AboutUsViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'about_elements', AboutUsViewSet, basename='about_element')
router.register(r'contact_messages', ContactMessageViewSet, basename='contact_message')
router.register(r'contacts', ContactViewSet, basename='contact')


urlpatterns = [
    path('', include(router.urls)),
]
