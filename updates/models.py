# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.db import models
from django.conf import settings

from django.core.serializers import serialize
# Create your models here.

def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
	# def serialize(self):
	# 	qs = self
	# 	return serialize("json", qs, fields=('user','content', 'image'))

	def serialize(self):
		qs = self
		final_array = []
		for obj in qs:
			stuct = json.loads(obj.serialize())
			# final_array.append(obj.serialize())
			final_array.append(stuct)
		# return final_array
		return json.dumps(final_array)

class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = UpdateManager()

	def __str__(self):
		return self.content or ""

	def serialize(self):
		json_data = serialize("json", [self], fields=('user','content', 'image'))
		stuct = json.loads(json_data)
		print(stuct)
		data = json.dumps(stuct[0]['fields'])
		return data