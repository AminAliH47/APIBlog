from django.contrib import admin
from blog.models import Articles, ArticlesCategory


# Register Articles model in admin
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'lang', 'status',)


admin.site.register(Articles, ArticlesAdmin)


# Register Articles category model in admin
class ArticlesCategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'lang',)


admin.site.register(ArticlesCategory, ArticlesCategoryAdmin)
