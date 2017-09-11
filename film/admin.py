from django.contrib import admin

# Register your models here.

from film.models import FILM,ACTOR,YEAR,DIRECTOR,COUNTRY,TYPE

class FILMAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(FILM,FILMAdmin)
admin.site.register(DIRECTOR)
admin.site.register(ACTOR)
admin.site.register(YEAR)
admin.site.register(TYPE)
admin.site.register(COUNTRY)