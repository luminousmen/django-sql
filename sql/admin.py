from django.contrib import admin

from .sqlapp import SQL


@admin.register(SQL)
class SQLAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
