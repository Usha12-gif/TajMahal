from  django.shortcuts import render    


def index(request):
    return render(request, 'index.html')
def images(request):
    return render(request, 'images.html')
def history(request):
    return render(request, 'history.html')
def night_view(request):
    return render(request, 'Night_view.html')
def contact_us(request):
    return render(request, 'contact_us.html')