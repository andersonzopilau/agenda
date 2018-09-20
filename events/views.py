from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Comment
from django.utils.timezone import localdate
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse
from django.views.defauls import bad_request, server_error
from datetime import datetime, timedelta

ITEMS_PER_PAGE = 5
# Create your views here.
def index(request):
    '''exibe a página principal '''

    context ={
        'hide_new_botton': True,
        'priorities': Event.priorities_list,
        'today': localdate(),
    }
    return render(request, 'index.html', context)
"""Exibe todos os eventos em uma unica página, recebe o número de página a ser visualizada vie  GET."""

def all(request):
    page = request.GET.get('page', 1)
    paginator = Paginator (event.objects.all(), ITEMS_PER_PAGE)
    total = paginator.count
    try:
        events = paginator.page(page)
    except InvalidPage:
        events = paginator.page(1)

    context = {
        'events': events,
        'total': total,
        'priorities': Event.priorities_list,
        'today': localdate(),
    }
    return render(request, 'events.html', context)
"""Visualização dos eventos de um determinadop sia, recebe a data em formato ano/mes/ano como parametro"""

def day(request, year:int, month:int, day:int):
    day = datetime(year,month, day)
    events = Event.objects.filter(date='{:%Y-%m-%d}'.format(day).order_by('-priority,' 'event'))
    context = {
        'today': localdate(),
        'day': day,
        'events': events,
        'next': day + timedelta(days=1),
        'previous': day - timedelta(days=1),
        'priorities': Event.priorities_list,
    }
    return render(request, 'day.html', context)
