import requests

api_key = 'd191593d9e4945bebef143606250112'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}"
)

response = weather_data

if response.status_code == 200:
    data = response.json()
    
    print("City---------:",data["location"]["name"])
    print("Country------:",data['location']['country'])
    print("Temperature C:",data['current']['temp_c'])
    print("Condition----:",data["current"]["condition"]["text"])
    print("Humidity-----:",data["current"]["humidity"])
    print("Wind (kph)---:",data["current"]["wind_kph"])
else:
    print("Error:",response.status_code, response.text)