from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&units=metric&appid=f09b7d6a001cf44acbe35ac21b905c51').read()
        list_of_data=json.loads(source)
        data={
        "country_code":str(list_of_data['sys']['country']),
        "coordinate":str(list_of_data['coord']['lon']) +','
        + str(list_of_data['main']['pressure']),
        "temp":str(list_of_data['main']['pressure']),
        "pressure":str(list_of_data['main']['pressure']),
        "humidity":str(list_of_data['main']['humidity']),
        "main":str(list_of_data['weather'][0]['main']),
        "description":str(list_of_data['weather'][0]['description']),
        "icon":list_of_data['weather'][0]['icon'],
        }
    else:
        data={}
    return render(request,'index.html',{'data':data})
