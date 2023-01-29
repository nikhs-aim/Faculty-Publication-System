from django.contrib import admin
from .models import Faculty
from .models import Conference,Journal,Post,Event


class FacultyAdmin(admin.ModelAdmin):
    readonly_fields = ('fac_id',)


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Conference)
admin.site.register(Journal)
admin.site.register(Post)
admin.site.register(Event)