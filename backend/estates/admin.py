from django.contrib import admin
from .models import Estate
# Register your models here.


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
	list_display = ('title', 'image',)
