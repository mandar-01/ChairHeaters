from django.contrib import admin

# Register your models here.
from .models import upload

class UploadModelAdmin(admin.ModelAdmin):
	class Meta:
		model = upload


admin.site.register(upload,UploadModelAdmin)