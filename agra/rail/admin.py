from django.contrib import admin
from .models import User,Train,Tinfo,Station

# Register your models here.
admin.site.register(User)
admin.site.register(Train)
admin.site.register(Tinfo)
admin.site.register(Station)
