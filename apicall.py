import requests


response = requests.get("https://dog.ceo/"
                         "api/breeds/image/random")
# response is now equal to a requests get request object.


json_response = response.json()
# this takes the response object and gets the content of the response, as json.
# it get's converted a dictionary
# at this point json_response looks like:
# {'message': 'https://images.dog.ceo/breeds/terrier-sealyham/n02095889_1458.jpg', 'status': 'success'}

dog_link = json_response['message']
# dog link should now be equal to the link
print(dog_link)









parameters = {'lat':0, 'lon':0, 'appid':'7d7da9cec04671cc03ef4220ca73d0bf'}
# These are parameters to be passed to the API, lat and lon are coordinates, appid basically
# just tells the API that i have access and am allowed to use it

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather", params=parameters)
# making the request, with the parameters
weather_json = response.json()
'''
Weather json now equal:
{'coord': {'lon': 0, 'lat': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 
'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 
'main': {'temp': 300.73, 'feels_like': 303.03, 'temp_min': 300.73, 'temp_max': 300.73, 'pressure': 1013, 
         'humidity': 70, 'sea_level': 1013, 'grnd_level': 1013}, 
'visibility': 10000, 'wind': {'speed': 5.56, 'deg': 181, 'gust': 5.5}, 
'clouds': {'all': 90}, 'dt': 1620394729, 'sys': {'sunrise': 1620366784, 'sunset': 1620410400}, 
'timezone': 0, 'id': 6295630, 'name': 'Globe', 'cod': 200}
'''
# kind of long and a little intimidating but thats no issue, it just takes some sorting out what you need
print(weather_json['weather'][0]['description'])
