from django.urls import path
from .views import (
    list_tweet, add_tweet, add_tweet_by_form, 
    add_tweet_by_model_form, RegisterView,
    delete_tweet
)

app_name = 'tweet_app'

urlpatterns = [
    path('', list_tweet, name='list_tweet'),
    path('add/', add_tweet, name='add_tweet'),
    path('add-by-form/', add_tweet_by_form, name='add_tweet_by_form'),
    path('add-by-model-form/', add_tweet_by_model_form, name='add_tweet_by_model_form'),
    path('delete/<int:id>/', delete_tweet, name='delete_tweet'),
    path('register/', RegisterView.as_view(), name='register'),
]