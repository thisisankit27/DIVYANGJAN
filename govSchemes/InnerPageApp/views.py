from django.shortcuts import render

# Create your views here.


def physicalDisability(request):
    return render(request, 'Disability Pages/physicalDisability.html')


def intellectualDisability(request):
    return render(request, 'Disability Pages/intellectualDisability.html')


def mentalDisability(request):
    return render(request, 'Disability Pages/mentalDisability.html')


def bloodDisorder(request):
    return render(request, 'Disability Pages/bloodDisorder.html')
