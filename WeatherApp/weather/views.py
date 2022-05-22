from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.
def index(arg):
    appid = "3168a8c73e1b4505548a05756b3518c1"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if arg.method == "POST":
        form = CityForm(arg.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            "city": city,
            "temp": res["main"]["temp"],
            "icon": res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {"all_info": all_cities, "form": form}

    return render(arg, "weather/index.html", context)
