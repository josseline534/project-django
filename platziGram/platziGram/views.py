from django.http import HttpResponse
""" Utils """
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%dth, %b %Y - %H:%M hrs')
    return HttpResponse(f'Hola Josselincita son las {now}')


def sorted_func(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_int = sorted(numbers)
    res_data = {
        'status': 'OK',
        'numbers': sorted_int,
        'message': 'Integers sorted sussessfully'
    }
    """ import pdb
    pdb.set_trace() """
    return HttpResponse(json.dumps(res_data), content_type='application/json')


def say_hi(request, name, age):
    print(name, age)
    if age < 12:
        message = f'{name} eres menor de {age} años'
    else:
        message = f'{name} eres mayor de {age} años'
    return HttpResponse(message)
