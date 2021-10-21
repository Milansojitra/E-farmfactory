from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

class post(models.Model):
    """Model definition for post."""
    title=models.CharField(max_length=100)
    content=RichTextUploadingField()
    date_posted=models.DateField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    tags=TaggableManager(blank=True)
    Video = models.FileField(upload_to="media/video/%y",blank=True,null=True)

    class Meta:
        """Meta definition for post."""
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postlist")
    
