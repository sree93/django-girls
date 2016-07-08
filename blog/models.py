from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	"""Post Model"""
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(default=None, blank=True, null=True)

	def publish(self):
		if(self.published_date == None):
			self.published_date = timezone.now()
			self.save()
			return True
		return False

	def __str__(self):
		return self.title