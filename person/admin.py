from django.contrib import admin
from django.forms import Textarea

from .models import *


# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zip_code')


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
    list_display = ('id', 'profession')


class AdditionalInfoInline(admin.StackedInline):
    model = AdditionalInfo
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
    }

    fieldsets = (
        (None, {
            'fields': (('start_finish', 'profession', 'academy'),  ('icon', 'content'))
        }),
        ('Skill info', {
            'fields': (('name', 'percent', 'is_main'), )
        }),
    )
    extra = 0


class ResumeAdmin(admin.ModelAdmin):
    inlines = [AdditionalInfoInline]
    list_display = ('id', 'type', 'is_skill', 'created_at')
    list_filter = ('is_skill', 'created_at')


admin.site.register(About, AboutAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Partner)
admin.site.register(Projects, ProjectAdmin)
