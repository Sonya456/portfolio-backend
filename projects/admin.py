from django.contrib import admin
from .models import Project, ProjectElement
from .models import AboutElement
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)

#admin.site.register(Contact, ContactAdmin)

class AboutElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'content', 'order')
    list_filter = ('type', 'order')
    search_fields = ('content',)

admin.site.register(AboutElement, AboutElementAdmin)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(ProjectElement)
class ProjectElementAdmin(admin.ModelAdmin):
    list_display = ('project', 'type', 'order')
    search_fields = ('project__title', 'type')
