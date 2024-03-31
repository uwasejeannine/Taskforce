

from django.contrib import admin
from .models import Category, Subcategory, Transaction, Budget

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Transaction)
admin.site.register(Budget)
