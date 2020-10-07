from django.db import models


class ContentManager(models.Manager):

    def get_content(self, category, home=True):
        result = self.filter(
            category__name=category
        )
        if category == 'Importante':
            if home:
                return result.order_by('-created')[:4]
            else:
                return result.order_by('-created')
        else:
            if category == 'Capacitación':
                return result.order_by('-created')[:2]
            else:
                return result.order_by('id')

    def get_data(self, category):
        print(titulo)
        result = self.get(
            title=titulo
        )
        print(result)
        return result
