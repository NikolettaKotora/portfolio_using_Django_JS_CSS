from django.contrib import admin
from .models import Tag, Project, ProjectImage
# Register your models here.

class ProjectImageInLine(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInLine]
    search_fields = ("title", "descreption")
    list_filter = ("tags",)

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

#Custom registration of the modules
admin.site.register(Tag, TagAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectImage)
