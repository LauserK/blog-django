from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

class Tag(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Comment(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
  date = models.DateField(auto_now_add=True)
  likes = models.IntegerField(default=0)
  content = models.TextField()
  parent = models.ForeignKey("self", verbose_name=("comment_parent"), on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

  def __str__(self):
    return "%s - %s" % (self.author.first_name, self.content)

class Article(models.Model):
  title = models.CharField(max_length=140)
  slug = models.SlugField(null=False, unique=True)
  content = HTMLField()
  likes = models.IntegerField(default=0)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
  visible = models.BooleanField(default=True)  
  date = models.DateField(auto_now_add=True)
  tags = models.ManyToManyField(Tag, blank=True)
  comments = models.ManyToManyField(Comment, blank=True)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.slug:
      # if not exists a slug, create one with the title
      self.slug = slugify(self.title)
    return super().save(*args, **kwargs)