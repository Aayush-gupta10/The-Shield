from django.contrib import admin
from .models import User,Member
class detail(admin.ModelAdmin):
   fieldsets = [
        (None,               {'fields': ['username']}),
        (None,               {'fields': ['password']}),
            ]
admin.site.register(User, detail)
admin.site.register(Member)

# Register your models here.
