from django.contrib import admin

from .models import Pay

class PayAdmin(admin.ModelAdmin):

    pass

admin.site.register(Pay, PayAdmin)