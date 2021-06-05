from django.contrib import admin

# Register your models here.
from .models import Rice
from .models import Paddy

admin.site.register(Rice)
admin.site.register(Paddy)