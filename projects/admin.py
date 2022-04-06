from django.contrib import admin
from projects.models import Collection

# Register your models here.


class CollectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Collection, CollectionAdmin)
