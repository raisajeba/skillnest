from django.contrib import admin
from .models import Skill,Category,SkillImage

class SkillImageInline(admin.TabularInline):
    model = SkillImage
    extra = 1  # default

class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillImageInline]

admin.site.register(Category)
admin.site.register(Skill,SkillAdmin)



# Register your models here.
