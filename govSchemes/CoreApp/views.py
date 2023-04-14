from django.shortcuts import render, redirect
from .models import SchemeList, Counts
import random

# Create your views here.


def index(request):
    
    #[Start] GET IP-Address
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    ip = get_ip(request)
    user_ip = Counts(user = ip)
    user_ip.save()
    result = Counts.objects.all().count()
    #[END] GET IP-Address
    
    dataDB = {
        'visit_count': result,
    }
    return render(request, 'index.html', dataDB)


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