from django.shortcuts import render
import requests
import random


def home(request):
    return render(request, "gifApp/home.html")

def view(request):
    response = requests.get("https://api.giphy.com/v1/gifs/search?api_key=hG7EChQ3ssxo96CFrMJp9dja3geapPBm&q=gaming&limit=25&offset=0&rating=g&lang=en")
    gifList = response.json()['data']
    total = len(gifList)
    gifs = []
    for i in range(total):
        gifs.append(gifList[i]['images']['original']['url'])
    context = {
        'gifs': gifs
    }
    return render(request, "gifApp/view.html", context)

def create(request):
    return render(request, "gifApp/create.html")