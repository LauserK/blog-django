from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article, Comment

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
        comments = article.comments.filter(parent__isnull=True)

        

        template_name = "single.html"
        context = {
            "article": article,
            "comments": comments
        }
        return render(request, template_name, context)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        comments = article.comments.filter(parent__isnull=True)

        id_parent = request.POST.get('span-answer')
        comment_body = request.POST.get('body')
        
        if (id_parent and comment_body) and (id_parent != '' and comment_body != ''):
            comment = Comment()
            comment.author = request.user
            comment.content = comment_body            

            if id_parent != 'post':
                comment.parent = Comment.objects.get(pk=id_parent)

            comment.save()

            if id_parent == 'post':
                article.comments.add(comment)
        
        template_name = "single.html"
        context = {
            "article": article,
            "comments": comments
        }
        return render(request, template_name, context)