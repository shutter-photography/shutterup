from django.contrib import admin
from .models import POST,UPDATE
# Register your models here.

class PageAdmin(admin.ModelAdmin):

    fields = ['Name']

    search_fields = ['Name']



admin.site.register(POST)
admin.site.register(UPDATE)
