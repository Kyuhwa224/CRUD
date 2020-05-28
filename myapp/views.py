from django.shortcuts import render, redirect
from .models import Cafe

def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'create.html')

def create_pro(request):
    cafe_product = Cafe()
    cafe_product.product_name = request.GET['product_name']
    cafe_product.product_price = request.GET['product_price']
    cafe_product.save()

    return redirect('index')

def show(request):
    products = Cafe.objects
    return render(request, 'show.html', {'products':products})

def updateSearch(request):
    products = Cafe.objects
    return render(request, 'updateSearch.html', {'products':products})

def search(request): 
    product = Cafe.objects.filter(product_name=request.GET['product_name'])
    return render(request, 'update.html', {'product':product[0]})

def update(request):
    product = Cafe.objects.filter(pk=request.GET['product_id'])[0]
    product.product_name = request.GET['product_name']
    product.product_price = request.GET['product_price']
    product.save()
    return redirect('index')

def deleteSearch(request):
    return render(request, 'deleteSearch.html')

def find(request):
    products = Cafe.objects.filter(product_name__contains=request.GET['product_name'])
    product = [] #바구니 
    for i in products: 
        product.append(i) #product 는 바구니 / products 는 뭘까?
    
    return render(request, 'delete.html', {'products':product}) #리스트 형태로 delete.html로 보내진다. 

def delete(request): 
    check_list = request.GET.getlist('chk') #체크된것이 리스트 형태로 넘어온다. 

    product = Cafe.objects.filter(product_name__in =check_list) #check_list 안에 있는지 없는지 확인해준다. 그 이름이 있어? 
    product.delete()
    return redirect ('index')