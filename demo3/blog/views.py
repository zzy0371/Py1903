from django.shortcuts import render
from django.views.generic import View,ListView,DetailView
# Create your views here.

class IndexView(View):
    def get(self,req):
        return render(req,"blog/index.html")

class SingleView(View):
    def get(self,req,id):
        return render(req, "blog/single.html")
