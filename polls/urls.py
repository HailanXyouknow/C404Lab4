from django.urls import path

# This is the MYSITE/POLLS/URLS.PY

#this is the file that consulted by Django if the URL starts with

from . import views

urlpatterns = [
    path('', views.index, name='index'), # http://127.0.0.1:8000/polls/ + ''
    path('<int:question_id>/', views.detail, name='detail'), # .../polls/5/
    path('<int:question_id>/results/', views.results, name='results'), # .../polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),  # ex: .../polls/5/vote/
]
