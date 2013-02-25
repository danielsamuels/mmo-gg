from django.contrib import admin
from models import Character, Level, Type


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "type", "user")
    list_filter = ("type", "user")

admin.site.register(Character, CharacterAdmin)
admin.site.register(Level)
admin.site.register(Type)
