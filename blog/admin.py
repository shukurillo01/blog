from django.contrib import admin
from .models import Blog
# Register your models here.
admin.site.register(Blog)
admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display=['sarlovha,vaqt']
    search_fields = ['sarlovha']