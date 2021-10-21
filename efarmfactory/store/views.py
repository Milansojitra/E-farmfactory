from django.shortcuts import render,get_object_or_404
from .models import product,order,orderItem
from .models import *
from django.http import JsonResponse
import json
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import product,order,orderItem

# Create your views here.
# def store(request):
#     if request.user.is_authenticated:
#         Customer=request.user
#         Order,created= order.objects.get_or_create(customer=Customer,complete=False)
#         items=Order.orderitem_set.all()
#     else:
#         items=[]
#         Order={'get_total_amount':0}


#     products=product.objects.filter(is_sold=False)
#     cont={'products':products}
#     return render(request,'store/store.html',context=cont)
@login_required
def cart(request):
    if request.user.is_authenticated:
        Customer=request.user
        Order,created= order.objects.get_or_create(customer=Customer,complete=False)
        items=Order.orderitem_set.all()
        cont={'items':items,'Order':Order}
    else:
        items=[]
        Order={'get_total_amount':0}
        cont={'items':items,'Order':Order}
    return render(request,'store/cart.html',context=cont)



def checkout(request):
    if request.user.is_authenticated:
        Customer = request.user
        Order,created= order.objects.get_or_create(customer=Customer,complete=False)
        items=Order.orderitem_set.all()
        cont={'items':items,'Order':Order}
    else:
        items=[]
        Order={'get_total_amount':0}
        cont={'items':items,'Order':Order}
    return render(request,'store/checkout.html',context=cont)

class PoductDetailView(DetailView):
    model=product
    template_name='store/product_detail.html'


class Product_tag_ListView(ListView):
    model=product
    template_name='store/store.html'
    context_object_name='products'
    ordering=['-date_posted']
    def get_queryset(self):
        return product.objects.filter(tags__slug=self.kwargs.get('slug'),is_sold=False)


class store(ListView):
    model=product
    template_name='store/store.html'
    ordering=['-date_posted']
    context_object_name='products'
    
    
    def get_queryset(self):
        return product.objects.filter(is_sold=False)

class store_search(ListView):
    model=product
    template_name='store/store.html'
    context_object_name='products'
    ordering=['-date_posted']
    
    def get_queryset(self):
        query=self.kwargs.get('query')
        return product.objects.filter(Q(name__icontains=query)|Q(city__icontains=query)|Q(description__icontains=query)|Q(tags__slug__icontains=query)).distinct().filter(is_sold=False)



class PoductCreateView(LoginRequiredMixin,CreateView):
    model=product
    template_name='store/product_Create.html'
    fields=['product_image','name','quantity','price','description','city','tags']
    def form_valid(self, form):
        form.instance.owner=self.request.user
        form.instance.is_sold=False
        return super().form_valid(form)


def UpdateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('action',action)
    print('productid',productId)

    Customer=request.user
    Order,created= order.objects.get_or_create(customer=Customer,complete=False)
        
    Product=product.objects.get(id=productId)
    OrderItem,created=orderItem.objects.get_or_create(order=Order,product=Product)

    if action=='add':
        pass
    elif action=='remove':
        OrderItem.delete()
    
    return JsonResponse('item was added',safe=False)



class productUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=product
    template_name='store/product_Create.html'
    fields=['product_image','name','quantity','price','description','city','tags']
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        product=self.get_object()
        if self.request.user==product.owner and product.is_sold==False:
            return True
        return False

class owner_ListView(LoginRequiredMixin,ListView):
    model=product
    template_name='store/my_product.html'
    context_object_name='products'
    ordering=['-date_posted']
    def get_queryset(self):
        return product.objects.filter(owner=self.request.user)

class productDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=product
    template_name='store/product_delete.html'
    success_url='/product/owner/'
    def test_func(self):
        product=self.get_object()
        if self.request.user==product.owner and product.is_sold==False:
            return True
        return False
