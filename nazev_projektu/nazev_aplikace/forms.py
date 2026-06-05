from django import forms
from django.utils.text import slugify
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "slug", "perex", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Název článku"}),
            "slug": forms.TextInput(attrs={"placeholder": "url-slug-clanku"}),
            "perex": forms.Textarea(attrs={"rows": 3, "placeholder": "Krátký popis článku…"}),
            "content": forms.Textarea(attrs={"rows": 10, "placeholder": "Obsah článku…"}),
        }
        labels = {
            "title": "Název",
            "slug": "URL slug",
            "perex": "Perex",
            "content": "Obsah",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-input")

    def clean_slug(self):
        slug = self.cleaned_data.get("slug") or slugify(self.cleaned_data.get("title", ""))
        return slug

