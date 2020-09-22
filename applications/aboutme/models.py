from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from applications.content.models import Content


class Fallo(TimeStampedModel):
    title = models.CharField('titulo', max_length=50)
    file = models.FileField('archivo', upload_to='Files')

    class Meta:
        verbose_name = 'Fallo'
        verbose_name_plural = 'Fallos'

    def __str__(self):
        return self.title


class Perfil(TimeStampedModel):
    foto_perfil = models.ImageField('imagen de perfil', upload_to='Profile')
    biography = RichTextUploadingField('biografia')
    full_info = models.ForeignKey(Content, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name_plural = 'Perfil'
