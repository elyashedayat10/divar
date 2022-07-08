from django.contrib import admin

from .models import Bookmark, Viewed, WantAd,Image


# Register your models here.
@admin.register(WantAd)
class WantAdAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created",
    )


admin.site.register(Viewed)
admin.site.register(Bookmark)
admin.site.register(Image)
