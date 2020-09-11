from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField


class Perfil(TimeStampedModel):
    foto_perfil = models.ImageField('imagen de perfil', upload_to='Profile')
    biography = RichTextUploadingField('biografia')
    links = models.TextField()

    class Meta:
        verbose_name_plural = 'Perfil'
