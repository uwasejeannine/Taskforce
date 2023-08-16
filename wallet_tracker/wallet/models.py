
# from django.db import models

# class Account(models.Model):
#     account_type = models.CharField(max_length=50)

#     def __str__(self):
#         return self.account_type

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name

# class Transaction(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_date = models.DateTimeField(auto_now_add=True)
#     description = models.TextField()

# class Budget(models.Model):
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)  
#     maximum_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.category} - {self.account}"

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} - {self.name}"
    

class Transaction(models.Model):
    account_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_type} - {self.amount} - {self.category}"
class Budget(models.Model):
    limit = models.DecimalField(max_digits=10, decimal_places=2)
