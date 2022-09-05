#import datetime
from datetime import datetime
import requests, json

# rating_url to find the top rated beach in Sydney
rating_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&input=top%20beaches%20Sydney&inputtype=textquery&key=AIzaSyDfyct62Zw9snqHqv9D14NngWTcV386TYM"
y = requests.get(rating_url).json()
beach_array = y["candidates"]
for j in range(len(beach_array)):
    formatted_address = beach_array[j]['formatted_address']

    #latitude_num = beach_array[j]['geometry']
    #converted_name = json.dumps(geometry_name)
    #print(formatted_address)

# base_url variable to store url
base_url = "https://api.weatherbit.io/v2.0/forecast/daily?&lat=-33.781&lon=151.290&key=307c636c4c304723ac1a77a5277a1b67"
response = requests.get(base_url)
# format = "%y%m%d"
x = response.json()
json_array = x["data"]
city_name = x["city_name"]
#print(city_name)
# store the value corresponding
for i in range(len(json_array)):

    # print('datetime: ', json_array[i]['datetime'])
    # fetching date time from url
    date_data = json_array[i]['datetime']
    temp = json_array[i]['temp']
    wind_speed = json_array[i]['wind_spd']
    uv = json_array[i]['uv']

    # converting date into required format
    modified_date = datetime.strptime(date_data, '%Y-%m-%d')
    # fetching weekday number  and checking it is friday or monday
    if modified_date.isoweekday() == 1 or modified_date.isoweekday() == 0:
        if 12 <= temp <= 30 and 3 <= wind_speed <= 9 and uv <= 12:
            print(formatted_address)
            print("Surfing suitable on:", modified_date, " with temperature : ", temp, "Wind speed :", wind_speed, " and uv : ", uv)