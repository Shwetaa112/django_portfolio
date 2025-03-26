from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# class certificate(models.Model):
#     # file = models.FileField(upload_to='certificate/')
#     # uploaded_at = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=100)
#     issued_by = models.CharField(max_length=100)
#     date_issued = models.DateField()
#     recipient = models.CharField(max_length=100)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    resume_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(default="hello",max_length=100)
    # issued_by = models.CharField(max_length=100)
    # date_issued = models.DateField()
    file = models.FileField(upload_to='certificate/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title=models.CharField(max_length=260)
    description = RichTextUploadingField()
    image=models.ImageField(upload_to='blogimage/')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title