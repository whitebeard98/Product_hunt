from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def home(request):
    product=Products.objects
    return render(request,'products/home.html',{'product':product})

@login_required(login_url="/accounts/signup")
def add(request):
    if request.method=="POST":
        print('is this a post request')
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            product=Products()
            product.title=request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url="http://"+request.POST['url']
            product.hunter=request.user
            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            product.date=timezone.datetime.now()
            product.save()
            return redirect('/products/'+str(product.id))
        else:
            return render(request,'products/add.html',{'error','error->All feilds must be field'})
        
    return render(request, 'products/add.html')

def detail(request,product_id):
    product=get_object_or_404(Products, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})
    
@login_required
def upvote(request,product_id):
    if request.method=="POST":
        product=get_object_or_404(Products,pk=product_id)
        product.upvote+=1
        product.save()
        return redirect('/products/' + str(product.id))
    