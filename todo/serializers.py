from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
	date_added = serializers.ReadOnlyField()

	class Meta:
		model = ToDo
		fields = ['title', 'description', 'date_added']

