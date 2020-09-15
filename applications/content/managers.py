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

    def get_detailed_data(self, titulo):
        print(titulo)
        result = self.get(
            title=titulo
        )
        print(result)
        return result
