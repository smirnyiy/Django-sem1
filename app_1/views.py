#from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse
from random import randint, choice
from .models import Coin, Author, Post

def index(request):
    logger.info('index get request')
    return HttpResponse ('Hello, World!')

def about(request):
    logger.info('about get request')
    return HttpResponse ('About as!')

def hat(request):
    heads_tails = choice(['Орел', 'Решка'])
    if heads_tails == 'Орел':
        res = 1
    else:
        res = 0
    logger.info(f'Монетка выпала стороной {heads_tails}')
    coin = Coin(side=res)
    coin.save()
    my_dict = Coin.get_data(3)
    return HttpResponse (f'Монетка выпала стороной {heads_tails}, {my_dict}')

def digit(request):
    logger.info('Random number from 0 to 100')
    return HttpResponse (randint(0, 100))

def dice(request):
    logger.info('Random number dice from 1 to 6')
    return HttpResponse (randint(1, 6))

logger = logging.getLogger(__name__)


def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)


def posts_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)