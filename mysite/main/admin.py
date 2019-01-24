from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


# do not give space in fields, like " tutorial_title". It will throw and exception of field error
#here we can filter what fields we can show in the page. Like we have here added three fields 	
class TutorialAdmin(admin.ModelAdmin):
	#we can use like this 
	'''fields = ["tutorial_title",
			  "tutorial_published",
			  "tutorial_content"]'''
	#or we can separate each form fields like this
	fieldsets = [
		("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
		("Content",{"fields":["tutorial_content"]})
	]

	formfield_overrides = {
		models.TextField: {'widget':TinyMCE()}
	}

admin.site.register(Tutorial, TutorialAdmin)

# I almost forget TutorialAdmin. Remember that!!!!!!!!!
