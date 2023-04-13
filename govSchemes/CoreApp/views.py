from django.shortcuts import render, redirect
import random
from .models import SchemeList

# Create your views here.


def index(request):
    return render(request, 'index.html')


def filterScheme(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        state = request.POST['state']
        disabilityType = request.POST['disabilityType']
        benefitCriteria = request.POST['benefitCriteria']
        scheme = SchemeList.objects.filter(
            state=state, disabilityType=disabilityType, benefitCriteria=benefitCriteria)
        scheme_list_send = []
        flag = True

        for i in scheme:
            scheme_list_send.append(i)

        if len(scheme_list_send) == 0:
            flag = False

        random.shuffle(scheme_list_send)

        dataDB = {
            'name': name,
            'scheme_list': scheme_list_send,
            'flag': flag,
        }
        return render(request, 'filterPage.html', dataDB)
    else:
        return redirect('/#findScheme')
