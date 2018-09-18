from django.shortcuts import render
from .models import Event
from django.utils.timezone import localdate
# Create your views here.
def index(request):
    '''exibe a página principal '''

    context ={
        'hide_new_botton': True,
        'priorities': Event.priorities_list,
        'today': localdate(),
    }
    return render(request, 'index.html', context)
