from django.db import models

class QueryDB(models.Model):
	query_text = models.CharField(max_length = 100)

class OpinionSet(models.Model):
	query = models.ForeignKey(QueryDB, on_delete=models.CASCADE)

	positive_percents = models.IntegerField(default=1)
	obtain_time = models.IntegerField(default=1)