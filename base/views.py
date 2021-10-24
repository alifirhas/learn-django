from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    """Menampilkan halaman home

    Args:
        request ([string]): [menampilkan method dan data yang dikirim]

    Returns:
        [type]: [description]
    """
    return HttpResponse('Home Page') 

def rooms(request):
    """Menampilkan halaman room

    Args:
        request ([string]): [menampilkan method dan data yang dikirim]

    Returns:
        [type]: [description]
    """
    return HttpResponse('Rooms')