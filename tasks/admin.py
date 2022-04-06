from django.contrib import admin
from tasks.models import Image

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
