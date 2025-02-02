from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)  # Show question in the admin list
    search_fields = ('question',)  # Enable search functionality
