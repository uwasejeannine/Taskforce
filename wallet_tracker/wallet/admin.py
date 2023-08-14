from django.contrib import admin
from .models import Account, Transaction, Category,Budget

# Register your models with the admin interface
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Budget)

