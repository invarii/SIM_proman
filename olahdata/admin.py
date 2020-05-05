from .models import User
from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Wilayah
from .models import Jobtitle
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Wilayah)
admin.site.register(Jobtitle)
