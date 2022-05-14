from django.db import models

# Create your models here.


class ToDo(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField()
	date_added = models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.title)
