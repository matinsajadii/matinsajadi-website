from django.shortcuts import render, redirect
from django.views import View


class BlogView(View):
    def get(self, request):
        return render(request, "blog/blog.html")

    def post(self, request):
        pass


