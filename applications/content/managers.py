from django.db import models


class ContentManager(models.Manager):

    def get_important_content(self):
        return self.filter(
            category__name='Importante'
        ).order_by('-created')[:6]
