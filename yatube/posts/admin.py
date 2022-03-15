from django.contrib import admin

from .models import Group, Post, Comment, Follow


@admin.register(Post)
class AdminZonePost(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author", 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Group)
class AdminZoneGroup(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description",)
    list_filter = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "author", "text", "created")
    search_fields = ("post",)
    list_filter = ("post",)
    empty_value_display = "-пусто-"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "author")
    empty_value_display = '-пусто-'
