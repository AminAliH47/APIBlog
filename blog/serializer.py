from rest_framework import serializers
from blog.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ("id", "lang", "author", "title",
                  "slug", "body", "image",
                  "category", "created_at", "updated_at",
                  "status",
                  )
