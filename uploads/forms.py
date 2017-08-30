from uploads.models import upload
from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model = upload
		fields = [
		"title",
		"description",
		"username"
		]