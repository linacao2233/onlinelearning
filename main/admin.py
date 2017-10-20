from django.contrib import admin

from .models import *

# Register your models here.
class VideoInline(admin.StackedInline):
	model = Videos

class SubjectAdmin(admin.ModelAdmin):
	inlines = [VideoInline]
	search_fields = ['name', 'description']

admin.site.register(Subjects, SubjectAdmin)
admin.site.register(Videos)
