from django.shortcuts import render

def template(request):
    return render(request, 'third/homePage.html')

def contact(request):
    return render(request, 'third/contact.html', {'values': ['VOPROSI', '+345']})
