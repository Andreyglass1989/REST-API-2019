# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

import json
from .models import Update
from restapi.mixins import JsonResponseMixin
# Create your views here.

# def detail_view(request):
	# return render(request, template, {}) #return JSON data
	# return HttpResponse(get_template().render({}))

def json_example_view(request):
	data= {
		"count": 1000,
		"content": "Some new content"
	}
	json_data = json.dumps(data)
	# return JsonResponse(data)
	return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data= {
			"count": 1000,
			"content": "Some new content"
		}
		# json_data = json.dumps(data)
		return JsonResponse(data)
		# return HttpResponse(json_data, content_type='application/json')

class JsonCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data= {
			"count": 1000,
			"content": "Some new content"
		}
		return self.render_to_json_response(data)