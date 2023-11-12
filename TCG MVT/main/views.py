from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import HttpResponseNotFound

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP ',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increment_stock(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
            # Tambah satu pada jumlah stok
            product.stock += 1
            product.save()
            data = {'new_stock': product.stock}
            return JsonResponse(data)
        except Product.DoesNotExist:
            pass
    return JsonResponse({'error': 'Invalid Request'})

def decrement_stock(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
            # Kurangi satu dari jumlah stok jika lebih dari nol
            if product.stock > 0:
                product.stock -= 1
                product.save()
            data = {'new_stock': product.stock}
            return JsonResponse(data)
        except Product.DoesNotExist:
            pass
    return JsonResponse({'error': 'Invalid Request'})

def delete_product(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return JsonResponse({'success': 'Product deleted successfully'})
        except Product.DoesNotExist:
            pass
    return JsonResponse({'error': 'Invalid Request'})

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def clean_cookie(request):
    response = HttpResponse('Cleaning the cookie')
    response.delete_cookie('sessionid')  # Replace 'last_login' with the name of the cookie you want to clean
    return response

def get_product_json(request):
    products = Product.objects.filter(user=request.user)
    products_list = [model_to_dict(product) for product in products]
    return JsonResponse(products_list, safe=False)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, price=price, amount = amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_product_ajax(request, id):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(pk=id)
            product.delete()
            return JsonResponse({'status': 'success'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)
    