from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/post_list', views.post_list, name='post_list'),
    path('/oldest', views.oldest, name='oldest'),
    path('/python', views.python, name='python'),
    path('/sqlnosql', views.sqlnosql, name='sqlnosql'),
    path('/web', views.webdevelpment, name='web'),
    path('/scripting', views.scripting, name='scripting'),
]