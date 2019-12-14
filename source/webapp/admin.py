from django.contrib import admin

from django.contrib import admin
from webapp.models import Image, Comment, Like


class ImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'photo', 'sign', 'likenum', 'author', 'created_at']
    list_filter = ['author']
    list_display_links = ['pk']
    readonly_fields = ['created_at']


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
admin.site.register(Like)

