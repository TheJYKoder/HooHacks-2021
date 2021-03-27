from django.shortcuts import render
import requests
import random


def home(request):
    return render(request, "gifApp/home.html")

def view(request):
    response = requests.get("https://api.giphy.com/v1/gifs/search?api_key=hG7EChQ3ssxo96CFrMJp9dja3geapPBm&q=running&limit=25&offset=0&rating=g&lang=en")
    gifList = response.json()['data']
    total = len(gifList)
    i = random.randint(0, total-1)
    gif=gifList[i]['images']['original']
    #print(gifList[0])

    context = {
        'gif': gif['url']
    }
    return render(request, "gifApp/view.html", context)

def create(request):
    return render(request, "gifApp/create.html")