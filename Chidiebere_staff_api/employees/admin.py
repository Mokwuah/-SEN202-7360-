from django.contrib import admin

from .models import Manager, Intern, Address

admin.site.register(Manager)
admin.site.register(Intern)
admin.site.register(Address)


#http://127.0.0.1:8000/admin
