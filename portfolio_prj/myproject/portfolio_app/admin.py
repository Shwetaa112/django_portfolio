from django.contrib import admin
from .models import Resume,Certificate,BlogPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db import models

class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides={
        models.TextField:{'widget':CKEditorUploadingWidget()}
    }

# Register your models here.
admin.site.register(Certificate)
admin.site.register(Resume)
admin.site.register(BlogPost,BlogPostAdmin)
