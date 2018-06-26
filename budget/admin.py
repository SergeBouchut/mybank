from django.contrib import admin

from budget import models


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'description', 'amount')

admin.site.register(models.Transaction, TransactionAdmin)
admin.site.register(models.Category)
