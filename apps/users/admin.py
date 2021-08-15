from django.contrib import admin
from apps.users.models import Customer, Freelancer, Transaction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Freelancer)
admin.site.register(Transaction)