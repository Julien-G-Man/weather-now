from django.shortcuts import render
import json, urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=92b447d5b957e7ae96f29ca7ce182a71').read()
        json_data = json.loads(res)
        data =  {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k', # Celsius
            "temp_c": f"{float(json_data['main']['temp']) - 273.15:.2f}", # Kelvin
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "icon": json_data['weather'][0]['icon'],
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
