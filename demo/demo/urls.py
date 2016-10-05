from django.conf.urls import url
from django.contrib import admin

from sql.sqlapp import execute_sql

urlpatterns = [
    url(r'^admin/sql/(?:sql/)?$', execute_sql, name='sql'),
    url(r'^admin/', admin.site.urls),
]
