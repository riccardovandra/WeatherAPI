import requests
from config import api_key

url = 'http://api.openweathermap.org/data/2.5/weather?q='

city_name = input('Insert City name ')

metric = 'units=metric'

complete_url = url + city_name + '&' + metric + '&APPID=' + api_key

print(complete_url)

r = requests.get(str(complete_url))
r_dict = r.json()

print('Fetchging Weather Info:')
print(' ')
# print(r_dict)
print('City:', city_name)
print('Temperature:', r_dict['main']['temp'])
print('Temperature min:', r_dict['main']['temp_min'])
print('Temperature max:', r_dict['main']['temp_max'])
