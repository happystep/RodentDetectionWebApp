from django.shortcuts import render

# Create your views here.

def paginate(request):
    return render(request, 'rodent/index.html', {})
