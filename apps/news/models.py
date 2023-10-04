from django.db import models

from django.utils.translation import gettext_lazy as _

from apps.accounts.models import CustomUser


class News(models.Model):
    name = models.CharField(
        _('News'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to=f'news/{name}',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')


class Article(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=100,
    )
    description = models.TextField(
        _('Description'),
    )
    photo = models.ImageField(
        _('Photo'),
        upload_to=f'articles/{title}',
        blank=True,
        null=True,
    )
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')





