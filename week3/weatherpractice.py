import requests

apiKey = '61944ba7ae9656d99a75ed6356bf23b1'
# {'id': 524901, 'APPID': apiKey}

testUrl = 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=' + apiKey
resp = requests.get(testUrl)
if resp.status_code in [200, 201]:
    weatherData = resp.json()
    print("The weather in {} is {}.".format(weatherData['name'],
                                            weatherData['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))
