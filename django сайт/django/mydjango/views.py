from django.http import HttpResponse

from django.views.generic import TemplateView

from django.views.generic import ListView

from .models import Posting

from django.shortcuts import render, redirect


class IndexView(TemplateView):
    extra_context = {"title": "Base"}
    template_name = "mydjango/index.html"


# class PostListView(ListView):
#     model = Posting
#     extra_context = {"title": "Base"}
#     context_object_name = "posts"
#     template_name = "mydjango/blog.html"


