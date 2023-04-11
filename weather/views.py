from django.shortcuts import render, redirect
"""
We are importing json because the information that we will get from the api
will be in json format thus to filter and pass that json data we need to
import json.
"""
import json
import urllib.request
from django.contrib import messages
from . import config
# Create your views here.

"""
For weather information we will use an api called openweatherapi
on their website we get a api key we can use it.
"""


def index(request):
    data = {'city': None}

    if request.method == 'POST':
        city = request.POST['city']
        app_id = config.app_id

        if city == "":
            messages.info(request, "Please enter city name")

        else:
            # sending request to open openweatherapi
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}'.replace(' ', '%20')
            res = urllib.request.urlopen(url).read()
            json_data = json.loads(res)

            """
            if we pass {'city': city, 'data': data} as argument to render then
            to access values we need to write data.city, data.country_code,
            data.humidity etc because the values are accessed using the . operator

            Also for array the index are accessed using the .
            """

            data = {
                'city': city,
                'country_code': str(json_data['sys']['country']),
                'coordinate': str(json_data['coord']['lon']) + " " +
                    str(json_data['coord']['lat']),
                'temperature': str(json_data['main']['temp']) + 'k',
                'pressure': str(json_data['main']['pressure']),
                'humidity': str(json_data['main']['humidity']),
                'k': [1,2,3],
                }


    return render(request, 'index.html', data)
