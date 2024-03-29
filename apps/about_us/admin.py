from django.contrib import admin

from .models import AboutUs, AboutUsImage, AboutUsVideo, Contacts


class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 1


class AboutUsVideoInline(admin.TabularInline):
    model = AboutUsVideo
    extra = 1


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'title',
        'description',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'title',
        'description',
    )
    inlines = [
        AboutUsImageInline,
        AboutUsVideoInline,
    ]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'value',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'value',
    )