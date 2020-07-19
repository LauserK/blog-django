from django.contrib import admin
from .models import Article, Tag, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  readonly_fields = ('likes',)
  exclude = ('author',)
  prepopulated_fields = {'slug': ('title',)}
  filter_horizontal = ('tags',)
  
  def save_model(self, request, obj, form, change):
    if not obj.pk:
      # if is new article add author
      obj.author = request.user
    super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  pass