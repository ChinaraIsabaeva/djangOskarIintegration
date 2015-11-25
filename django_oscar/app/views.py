from django.shortcuts import render

from django_oscar.lib.get_data import collect_final_data


def home(request):
    data = collect_final_data()
    return render(request, 'home.html', data)