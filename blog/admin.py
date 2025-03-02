from django.contrib import admin
from .models import Publications

# Register your models here.
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'updated')
    list__filter = ('author', 'date', 'updated')
    search_fields = ('title', 'body', 'author__username')
    ordering = ('-date',)
    

admin.site.register(Publications, PublicationsAdmin)