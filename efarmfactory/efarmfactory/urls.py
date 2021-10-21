from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.account_urls')),
    path('farmtube/',include('farmtube.farmtube_urls')),
    path('',include('store.store_urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += [
     path('upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 
