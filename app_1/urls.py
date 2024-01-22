from django.urls import path

from .views import index
from .views import about
from .views import hat
from .views import digit
from .views import dice

urlpatterns = {
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('hat', hat, name='hat'),
    path('dice/', dice, name='dice'),
    path('digit/', digit, name='digit'),
}
