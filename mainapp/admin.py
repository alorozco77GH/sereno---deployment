from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post, Contact

admin.site.register(Post)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
