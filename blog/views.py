from rest_framework import generics
from blog.mixins import LangMixinDetail, LangMixinList
from blog.serializer import ArticlesSerializer


class ArticlesList(LangMixinList, generics.ListAPIView):
    """ list of active articles """
    serializer_class = ArticlesSerializer


class ArticlesDetail(LangMixinDetail, generics.RetrieveUpdateDestroyAPIView):
    """ detail of active article """
    serializer_class = ArticlesSerializer
