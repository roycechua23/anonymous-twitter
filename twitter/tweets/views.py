from django.shortcuts import render, redirect
from .models import * 
# Create your views here.
def home(request):
    tweets = Tweets.objects.all().order_by("-date_posted")
    print(tweets)
    return render(request, "index.html", {
        "tweets":tweets
    })

def tweet(request):
    if request.method == "POST":
        name = request.POST["name"]
        title = request.POST["title"]
        message = request.POST["message"]
        t = Tweets.objects.create(name=name, title=title, message=message)
        t.save()
        return redirect("/")
    else:
        return redirect("/")