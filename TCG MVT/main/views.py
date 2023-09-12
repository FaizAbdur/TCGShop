from django.shortcuts import render
# Create your views here.

def show_main(request):
    context = {
        'title' : 'TCG SHOP',
        'name'  : 'Faiz ',
        'class' : 'PBP B'
    }

    return render(request, "main.html", context)
