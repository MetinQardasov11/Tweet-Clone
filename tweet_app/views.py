from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from .models import Tweet
from .forms import AddTweetForm, AddTweetModelForm

def list_tweet(request):
    tweets = Tweet.objects.all()
    context = {
        'tweets': tweets
    }
    return render(request, 'tweet_app/list-tweet.html', context)


@login_required(login_url='/login')
def add_tweet(request):
    if request.method == "POST":
        message = request.POST['message']
        Tweet.objects.create(username=request.user, message=message)
        return redirect('tweet_app:list_tweet')
    return render(request, 'tweet_app/add-tweet.html')

@login_required
def add_tweet_by_form(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            Tweet.objects.create(username=request.user, message=message)
        return redirect('tweet_app:list_tweet')
    
    form = AddTweetForm()
    return render(request, 'tweet_app/add-tweet-by-form.html', {'form': form})


@login_required
def add_tweet_by_model_form(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweet_app:list_tweet')
    
    form = AddTweetModelForm()
    return render(request, 'tweet_app/add-tweet-by-model-form.html', {'form': form})


@login_required
def delete_tweet(request, id):
    tweet = Tweet.objects.get(id=id)
    if tweet.username == request.user:
        tweet.delete()
        return redirect('tweet_app:list_tweet')
    return redirect('tweet_app:list_tweet')


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'