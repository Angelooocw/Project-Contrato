from django.db import models
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    title = models.CharField('titulo', max_length=50)
    description = models.TextField('Descripcion inicio')
    image = models.ImageField('Imagen', upload_to='Home', blank=True)

    class Meta:
        verbose_name = 'Pagina principal'
        verbose_name_plural = 'Pagina principal'

    def __str__(self):
        return self.title
