from django.contrib import admin
from .models import Event, Comment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("date", "event", "priority")
    list_display_links = ("event", )
    list_filter = ("date", "priority")
    list_editable = ("priority", )
    search_fields = ("event", "date")


admin.site.register(Comment)
