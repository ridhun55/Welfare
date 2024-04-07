from django.contrib import admin
from . import models  

admin.site.register(models.WelfarePost)
admin.site.register(models.PostCategoryEducation)
admin.site.register(models.PostCategoryHealth)
admin.site.register(models.ReportAnIssue)