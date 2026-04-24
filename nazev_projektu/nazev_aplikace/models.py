from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL slug")
    perex = models.TextField(max_length=400, verbose_name="Perex")
    content = models.TextField(verbose_name="Obsah")
    author = models.CharField(max_length=100, verbose_name="Autor")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Vytvořeno")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Upraveno")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Článek"
        verbose_name_plural = "Články"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("article_detail", kwargs={"slug": self.slug})
