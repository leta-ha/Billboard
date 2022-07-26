from django.contrib import admin
from django.urls import path
from chart.views import *

app_name = 'chart'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('<int:id>', detail, name='detail'),
    path('db', init_db, name='init_db'),
]