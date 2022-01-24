from django.contrib import admin
from .models import Image
from .models import Login
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ['id','name','password']

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','title','desc']