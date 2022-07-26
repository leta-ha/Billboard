from django.contrib import admin
from .models import Music, Producer, Writer

# Register your models here.
admin.site.register(Music)
admin.site.register(Producer)
admin.site.register(Writer)