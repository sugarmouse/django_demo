from django.urls import path

from . import views

#  带有命名空间的URL，可以防止多个应用中 url.name 重名的情况
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results', views.results, name="results"),
    path('<int:question_id>/vote', views.vote, name="vote"),
]
