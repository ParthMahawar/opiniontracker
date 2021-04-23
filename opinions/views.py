from django.shortcuts import render
from django.http import HttpResponse
from .Code.sentiment import sentiment
import matplotlib.pyplot as plt
from datetime import datetime
from .models import QueryDB, OpinionSet

# Create your views here.
def ask_for_query(request):
	return render(request, 'ask_for_query.html')

def return_opinions(request):
	time = str(int((datetime.utcnow()- datetime(2017,1,1)).total_seconds()))
	
	save = 'opinions/static/opinions/'+time+'.jpg'
	save2 = 'opinions/static/opinions/'+time+'neutral.jpg'
	save3 = 'opinions/static/opinions/'+time+'history.jpg'
	imgpath = 'opinions/' + time + '.jpg'
	imgpath2 = 'opinions/' + time + 'neutral.jpg'
	imgpath3 = 'opinions/' + time + 'history.jpg'
	
	query = request.GET['query']
	numtweets = int(request.GET['numtweets'])
	
	data = sentiment(query, numtweets)
	positive = data['positive']
	negative = data['negative']
	neutral = data['neutral']
	positive_percentage = data['percentage']
	negative_percentage = 100 - positive_percentage
	
	plt.pie([positive, negative], colors = ['green', 'red'], autopct='%1.1f%%', shadow = True)
	plt.axis('equal')
	plt.savefig(save)
	plt.clf()
	
	plt.pie([positive, negative, neutral], colors = ['green', 'red', 'gray'], autopct='%1.1f%%', shadow = True)
	plt.axis('equal')
	plt.savefig(save2)
	plt.clf()

	if query.lower() not in QueryDB.objects.values_list('query_text', flat = True):
		query_from_DB = QueryDB(query_text = query.lower())
		query_from_DB.save()

	else:
		query_from_DB = QueryDB.objects.get(query_text = query.lower())

	query_from_DB.opinionset_set.create(positive_percents = positive_percentage, obtain_time = int(time))

	percent_list = query_from_DB.opinionset_set.values_list('positive_percents', flat = True)
	time_list = query_from_DB.opinionset_set.values_list('obtain_time', flat = True)
	time_list = list(time_list)

	time_list = [round(value/86400, 2) for value in time_list]

	plt.plot(time_list, percent_list)
	plt.xlabel('Days since 1/1/2017')
	plt.ylabel('Percentage of positive opinions')
	plt.savefig(save3)
	plt.clf()
	
	context = {'imgpath3':imgpath3,'imgpath2':imgpath2,'imgpath':imgpath, 'time':time, 'query':query, 'positive':str(positive), 'negative':str(negative),'neutral':str(neutral)}
	
	return render(request, 'return_opinions.html', context)