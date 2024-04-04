from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
                
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST ['content'],
            category = request.POST['category']
        )
        return redirect('list')
    
    return render(request, 'new.html',{'categories': ['취미', '음식','프로그래밍']})

def list(request):
    unique_categories = ['취미', '음식', '프로그래밍']
    category_counts = {}
    for category in unique_categories:
        category_counts[category] = Article.objects.filter(category=category).count()
    total_articles = Article.objects.count()
    articles = Article.objects.all()
    return render(request, 'list.html', {'unique_categories': unique_categories, 'category_counts': category_counts, 'total_articles': total_articles, 'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(id =article_id)
    return render(request, 'detail.html', {'article': article})

def category_view(request, category):
    articles = Article.objects.filter(category=category)
    total_articles = articles.count()
    
    return render(request, 'category_view.html', {'articles':articles, 'category': category, 'total_articles': total_articles})