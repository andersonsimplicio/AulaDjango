from django.shortcuts import render
from django.views import View
from .models import Produto

class Home(View):
    template_name = "produto/index.html"

    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.filter(is_published=True)

        return render(request,self.template_name,{'produtos':produtos})
