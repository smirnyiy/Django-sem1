from django.urls import path

from .views import index
from .views import about
from .views import hat
from .views import digit
from .views import dice
from .views import authors_view
from .views import posts_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('hat', hat, name='hat'),
    path('dice/', dice, name='dice'),
    path('digit/', digit, name='digit'),
    path('authors/', authors_view, name='authors'),
    path('posts/', posts_view, name='posts'),
]
