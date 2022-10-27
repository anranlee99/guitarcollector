from django.contrib import admin
from .models import Guitar, Accessory, Servicing
# Register your models here.
admin.site.register(Guitar)
admin.site.register(Accessory)
admin.site.register(Servicing)