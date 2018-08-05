# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from django.http import HttpResponse


class homeView(View):
    def get (self, request, *args, **kwargs):
        return HttpResponse("This is the homeview")

class intChart(View):
    def get (self, request, *args, **kwargs):
        return render(request,'charts.html', {})