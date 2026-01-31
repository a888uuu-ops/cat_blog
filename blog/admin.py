from django.contrib import admin
from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
    )


admin.site.register(Cat, CatAdmin)
