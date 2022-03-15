from django.views.generic.base import TemplateView


class Tech(TemplateView):
    template_name = 'about/tech.html'


class About(TemplateView):
    template_name = 'about/author.html'
