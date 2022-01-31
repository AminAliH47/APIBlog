from blog.models import Articles


class LangMixinList:
    def list(self, request, *args, **kwargs):
        lang = request.headers['Accept-Language']
        self.queryset = Articles.objects.filter(status=True, lang=lang)
        return super().list(request, *args, **kwargs)


class LangMixinDetail:
    def retrieve(self, request, *args, **kwargs):
        lang = request.headers['Accept-Language']
        self.queryset = Articles.objects.filter(status=True, lang=lang)
        return super().retrieve(request, *args, **kwargs)
