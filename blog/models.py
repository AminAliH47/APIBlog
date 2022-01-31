from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from blog.managers import ArticlesManager

LANG = (
    ('fa', 'fa'),
    ('en', 'en'),
)


class ArticlesCategory(models.Model):
    """ Model for blog Articles category """

    # Fields
    lang = models.CharField(
        max_length=10,
        choices=LANG,
    )
    title = models.CharField(
        max_length=100,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    # Meta class
    class Meta:
        verbose_name_plural = "02. Categories"
        verbose_name = "category"
        ordering = ("created_at",)

    # Methods
    def __str__(self):
        return self.title


class Articles(models.Model):
    """ Model for blog Articles """

    # Fields
    lang = models.CharField(
        max_length=10,
        choices=LANG,
    )
    author = models.ForeignKey(
        to="account.User",
        on_delete=models.CASCADE,
        verbose_name=_("Author"),
    )
    title = models.CharField(
        max_length=120,
        verbose_name=_("Title"),
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=_("Slug"),
    )
    body = models.TextField(
        verbose_name=_("Article content"),
    )
    image = models.ImageField(
        upload_to="blog/articles",
        verbose_name=_("Article Image"),
    )
    category = models.ForeignKey(
        to=ArticlesCategory,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Category"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    status = models.BooleanField(
        default=False,
    )

    # Manager
    objects = ArticlesManager()

    # Metadata
    class Meta:
        verbose_name_plural = "01. Articles"
        verbose_name = "article"
        ordering = ("created_at",)

    # Methods
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("blog:detail", kwargs={"id": self.id, "slug": self.slug})
