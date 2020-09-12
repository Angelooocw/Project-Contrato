from django.db import models


class ContentManager(models.Manager):

    def get_content(self, category):
        result = self.filter(
            category__name=category
        )
        if category == 'Importante':
            return result.order_by('-created')[:6]
        else:
            return result.order_by('id')
