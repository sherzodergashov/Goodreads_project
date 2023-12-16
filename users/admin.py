from django.contrib import admin

from users.models import CustomUser

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['username', 'last_name', 'first_name']
    list_filter = ["username"]


admin.site.register(CustomUser, CustomerAdmin)
