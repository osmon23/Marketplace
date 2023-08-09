from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutUs(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
        null=True,
        blank=True,
    )
    title = models.CharField(
        _('Title'),
        max_length=255,
        null=True,
        blank=True,
    )
    description = models.TextField(
        _('Description'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('About Us')
        verbose_name_plural = _('About Us')


class AboutUsImage(models.Model):
    image = models.ImageField(
        _('Image'),
        upload_to='about_us_images/',
    )
    about_us = models.ForeignKey(
        AboutUs,
        verbose_name=_('About us'),
        related_name='image',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.about_us.name
    
    class Meta:
        verbose_name = _('About us image')
        verbose_name_plural = _('About us images')


class AboutUsVideo(models.Model):
    video = models.FileField(
        _('Video'),
        upload_to='about_us_videos/',
    )
    about_us = models.ForeignKey(
        AboutUs,
        verbose_name=_('About us'),
        related_name='video',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.about_us.name
    
    class Meta:
        verbose_name = _('About us video')
        verbose_name_plural = _('About us videos')
