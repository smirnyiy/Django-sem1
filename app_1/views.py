#from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse
from random import randint, choice

def index(request):
    logger.info('index get request')
    return HttpResponse ('Hello, World!')

def about(request):
    logger.info('about get request')
    return HttpResponse ('About as!')

def hat(request):
    logger.info('random name ')
    hads_tails = ['Орел', 'Решка']
    return HttpResponse (choice(hads_tails))

def digit(request):
    logger.info('Random number from 0 to 100')
    return HttpResponse (randint(0, 100))

def dice(request):
    logger.info('Random number dice from 1 to 6')
    return HttpResponse (randint(1, 6))

logger = logging.getLogger(__name__)