from uploads.models import upload
from django import forms

class PostForm(forms.ModelForm):
	#docfile = upload.docFile(required=False)
	class Meta:
		model = upload
		fields = [
		"title",
		"description",
		"docFile",
		]