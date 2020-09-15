from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import ContentManager


class Category(TimeStampedModel):
    name = models.CharField('nombre', max_length=30)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Content(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=50)
    short_title = models.CharField('Titulo corto', max_length=30, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail_img = models.ImageField('Imagen', upload_to='Content', blank=True)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    slug = models.SlugField(editable=False, max_length=200)

    objects = ContentManager()

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

    def __str__(self):
        return '{} {}'.format(self.id, self.title)

    def save(self, *args, **kwargs):
        slug_unique = '{}'.format(self.title)
        self.slug = slugify(slug_unique)
        super(Content, self).save(*args, **kwargs)
