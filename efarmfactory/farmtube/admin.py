from django.contrib import admin
from .models import post

class post_length(admin.SimpleListFilter):
    title = 'Lengthy'
    parameter_name = 'get_content'

    def lookups(self, request, model_admin):
        return (('length','Detailed_post'),
        ('short','Short_post'))

    def queryset(self, request, queryset):
        if self.value()=='length':
            return queryset.filter(len(get_content)>20)
        return queryset.filter(len(get_content)<=20)

class postAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post-detail', {
            "fields": (
                'title','author','date_posted'
            ),
        }),
        ('post', {
            "fields": (
                'content','tags','Video'
            ),
        }),
    )
    def get_content(self,post):
        if len(post.content)>10:
            return post.content[:10]
        return post.content
    
    list_display=['id','title','get_content','date_posted','author']
    search_fields=['id','title','content','date_posted','author']
    list_display_links=['id','get_content']
    list_editable=['title']
    list_filter=['date_posted','author']
    ordering=['-date_posted']
    actions_on_bottom=True

admin.site.register(post,postAdmin)

admin.site.site_header='e-Farmfactory'
admin.site.site_title='e-Farmfactory'
admin.site.index_title='admin pannel'