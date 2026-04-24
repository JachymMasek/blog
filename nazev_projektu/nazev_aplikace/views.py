from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def zkusebni_stranka(request):
    return render(request, 'zkusebni_stranka.html')


def article_list(request):
    q = request.GET.get("q", "").strip()
    articles = Article.objects.all()
    if q:
        articles = articles.filter(title__icontains=q) | articles.filter(author__icontains=q)
    return render(request, "article_list.html", {"articles": articles, "q": q})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "article_detail.html", {"article": article})


def article_create(request):
    form = ArticleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        article = form.save()
        messages.success(request, "Článek byl úspěšně vytvořen.")
        return redirect("article_detail", slug=article.slug)
    return render(request, "article_form.html", {"form": form, "action": "Nový článek"})


def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Článek byl upraven.")
        return redirect("article_detail", slug=article.slug)
    return render(request, "article_form.html", {"form": form, "action": "Upravit článek", "article": article})


def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        article.delete()
        messages.success(request, "Článek byl smazán.")
        return redirect("article_list")
    return render(request, "article_confirm_delete.html", {"article": article})