# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Update
# Create your views here.

# def detail_view(request):
	# return render(request, template, {}) #return JSON data
	# return HttpResponse(get_template().render({}))

def update_model_detail_view(request):
	data= {
		"count": 1000,
		"content": "Some new content"
	}
	return JsonResponse(data)