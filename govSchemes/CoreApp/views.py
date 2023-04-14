from django.shortcuts import render, redirect
from .models import SchemeList, VisitCounts, FilterCounts
import random

# Create your views here.

def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

def index(request):
    
    # [Start] GET IP-Address
    ip = get_ip(request)
    user = VisitCounts(user_ip = ip)
    user.save()
    #[END] GET IP-Address
    
    dataDB = {
        'visit_count': len(VisitCounts.objects.all()),
        'filter_count': len(FilterCounts.objects.all())
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
        
        #[START] Filteration-Count
        ip = get_ip(request)
        user = FilterCounts(user_ip = ip, username = name, userage=age)
        user.save()
        #[END] Filteration-Count

        dataDB = {
            'name': name,
            'scheme_list': scheme_list_send,
            'flag': flag,
        }
        return render(request, 'filterPage.html', dataDB)
    else:
        return redirect('/#findScheme')