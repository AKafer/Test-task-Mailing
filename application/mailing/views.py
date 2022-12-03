from django.shortcuts import render


def task(request):
    return render(request, 'index.html')
