from django.db import models


class ArticlesManager(models.Manager):
    def get_active_articles(self):
        return self.filter(status=True)

    def get_current_lang(self, lang):
        return self.filter(lang__icontains=lang)
