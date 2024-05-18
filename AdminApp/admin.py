from django.contrib import admin
from . import models  

admin.site.register(models.WelfarePost)
admin.site.register(models.PostCategoryEducation)
admin.site.register(models.PostCategoryHealth)
admin.site.register(models.PostCategoryEmployment)
admin.site.register(models.PostCategoryHousing)
admin.site.register(models.PostCategoryRuralDevelopment)
admin.site.register(models.PostCategoryMinorityWelfare)
admin.site.register(models.ReportAnIssue)
admin.site.register(models.Feedback)