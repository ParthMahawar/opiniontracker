from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^showopinion/', views.return_opinions, name='ReturnOpinion'),
    url(r'^$', views.ask_for_query, name='AskForQuery')
]