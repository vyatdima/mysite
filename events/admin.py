from django.contrib import admin
from events.models import Event, People, PeopleEvent, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_sorev', 'is_no_view')
    search_fields = ('name',)
    ordering = ('-date_sorev',)

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('fam', 'nam', 'ptr', 'brd', 'pk')
    search_fields = ('fam',)
    ordering = ('fam', 'nam', 'ptr', 'brd')

@admin.register(PeopleEvent)
class PeopleEventAdmin(admin.ModelAdmin):
    list_display = ('event', 'people',)
    search_fields = ('event', 'people')
    ordering = ('event', 'people')
    list_filter = ('event', 'people')
