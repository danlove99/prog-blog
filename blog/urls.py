from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'^/about$', views.about, name='about'),
    path(r'^/projects$', views.projects, name='projects'),
    path(r'^/DE$', views.DE, name='DE'),
    path(r'^/tutorials$', views.tutorials, name='tutorials')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
