from django.contrib import admin
from .models import User, Manager, Employee, Admin

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Admin)