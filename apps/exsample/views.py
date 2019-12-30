from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def main_view(request):
    """
    """
    return render(request, 'dct/index.html')


def get_all_person(request):
    """
    """
    return JsonResponse({
        'data': ['Tim', 'jerry', 'wstom']
    })
