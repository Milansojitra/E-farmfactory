from django.contrib import admin
from .models import product,order,orderItem
from import_export.admin import ImportExportModelAdmin
from django.db import models


admin.site.site_header='e-Farmfactory'

class productAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fieldsets=  [('Title/date_posted',{'fields':['product_image','name','quantity','price']}),
               ('Description-part',{'fields':['date_posted','description','owner','tags','is_sold','city']})
               ]
    search_fields=('title','content','description','city')
    list_display=('name','owner','date_posted','is_sold')
    list_filter=('owner','date_posted','city')
   
    formfield_overrides = {
        models.TextField: {},
        }
    
class orderAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fieldsets=  [('Customer',{'fields':['customer']}),
               ('complete',{'fields':['complete']})
               ]
    search_fields=('customer','complete')
    list_display=('customer','complete')
    list_filter=('date_posted','complete','customer')
   
    formfield_overrides = {
        models.TextField: {},
        }

admin.site.register(product,productAdmin)
admin.site.register(order,orderAdmin)
admin.site.register(orderItem)