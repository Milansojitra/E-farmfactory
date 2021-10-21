
from django.urls import path
from .views import (cart,checkout,store,PoductDetailView,
        Product_tag_ListView,PoductCreateView,UpdateItem,store_search,
        productUpdateView,owner_ListView,productDeleteView)

urlpatterns = [
    path('',store.as_view(),name='store'),
    path('cart/',cart ,name='cart'),
    path('checkout/',checkout ,name='checkout'),
    path('product/<int:pk>/', PoductDetailView.as_view(), name='product-detail'),
    path('product/create/', PoductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', productUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', productDeleteView.as_view(), name='product-delete'),
    path('product/owner/', owner_ListView.as_view(), name='owner-product'),
    path('update_item/', UpdateItem, name='update_item'),
    path('tag/<str:slug>/',Product_tag_ListView.as_view(), name='product-tag-list'),
    path('search/<str:query>/',store_search.as_view(), name='store-search'),


]
