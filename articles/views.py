from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article

class HomeView(View):
    def get(self, request):
        articles = Article.objects.filter(visible=True).order_by('-pk')
        template_name = "home.html"
        context = {
            "articles": articles
        }
        return render(request, template_name, context)

class SinglePostView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        template_name = "single.html"
        context = {
            "article": article
        }
        return render(request, template_name, context)