import random
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.db import connections
from .apps import get_rabbits 
from .models import Rabbit


def index(request):
    return render(request, 'main/main.html')


def setup(request):
    return render(request, 'main/setup.html')


def monitoring(request):
    if request.user.is_authenticated:
        rabbits = Rabbit.objects.all()
        print(rabbits)
        return render(request, 'main/monitoring.html', { 'rabbits': rabbits })
    else:
        return HttpResponseRedirect('authorization/login/')


def get_rabbits_data(request):
    rabbits = Rabbit.objects.all()
    data = [{'rabbit_id': rabbit.rabbit_id,
             'rabbit_name': rabbit.rabbit_name,
             'rabbit_temp': rabbit.rabbit_temp,
             'rabbit_temp_med': rabbit.rabbit_temp_med,
             'rabbit_pulse': rabbit.rabbit_pulse,
             'rabbit_pulse_med': rabbit.rabbit_pulse_med} for rabbit in rabbits]
    return JsonResponse(data, safe=False)


def post_test_data(request):
    rbt_connection = connections['rabbits']
    with rbt_connection.cursor() as cursor:
            cursor.execute("SELECT rabbit_temp_med, rabbit_pulse_med FROM rabbits_group_1")
            rows = cursor.fetchall()
            for i in range(len(rows)):
                get_temp = random.uniform(35, 44)
                med_temp = (rows[i][0] + get_temp) / 2
                get_pulse = random.uniform(80, 140)
                med_pulse = (rows[i][1] + get_pulse) / 2
                cursor.execute(f"""UPDATE rabbits_group_1 SET rabbit_temp={get_temp}, 
                rabbit_temp_med={med_temp}, 
                rabbit_pulse={get_pulse}, 
                rabbit_pulse_med={med_pulse} WHERE rabbit_id={i + 1}""")


def profile(request):
    return render(request, 'main/profile.html')
        