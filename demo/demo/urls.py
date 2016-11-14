from django.conf.urls import url
from django.contrib import admin

from sqlapp.sqlapp import execute_sql

urlpatterns = [
    url(r'^admin/sqlapp/(?:sql/)?$', execute_sql, name='sql'),
    url(r'^admin/', admin.site.urls),
]
