from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from . models import Category, Product
# Create your views here.


class HomeListView(ListView):

    template_name = 'home.html'

    def get(self,request):
        cats = Category.objects.all()

        return render(request, self.template_name,{'cats':cats})



class HomeDetailList(ListView):
    template_name = 'home_detail.html'


    def get(self,request,id):
        brand = Category



