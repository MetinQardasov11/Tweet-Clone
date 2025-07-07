from django.shortcuts import render, redirect
from .models import Tweet
from .forms import AddTweetForm, AddTweetModelForm

def list_tweet(request):
    tweets = Tweet.objects.all()
    context = {
        'tweets': tweets
    }
    return render(request, 'tweet_app/list-tweet.html', context)


def add_tweet(request):
    if request.method == "POST":
        username = request.POST['username']
        message = request.POST['message']
        Tweet.objects.create(username=username, message=message)
        return redirect('tweet_app:list_tweet')
    return render(request, 'tweet_app/add-tweet.html')


def add_tweet_by_form(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message = form.cleaned_data['message']
            Tweet.objects.create(username=username, message=message)
        return redirect('tweet_app:list_tweet')
    
    form = AddTweetForm()
    return render(request, 'tweet_app/add-tweet-by-form.html', {'form': form})



def add_tweet_by_model_form(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweet_app:list_tweet')
    
    form = AddTweetModelForm()
    return render(request, 'tweet_app/add-tweet-by-model-form.html', {'form': form})