from datetime import datetime
import requests, json, re

# google api to find the famous beach in Sydney
google_api_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address"

#google_keyword_search to key-in the user defined search parameter.
#famous beaches of Sydney or top beaches of Sydney or surfing beaches in Sydney etc
google_keyword_search = "&" + "input=top-rated%20beaches%20of%20Sydney&inputtype=textquery"
# Enter your API key here
google_api_key = "&"+ "key=AIzaSyDfyct62Zw9snqHqv9D14NngWTcV386TYM"

#Complete url for google api
rating_url = google_api_url+google_keyword_search+google_api_key

# json method of response object
# convert json format data into
# python format data
y = requests.get(rating_url).json()
beach_array = y["candidates"]
for j in range(len(beach_array)):
    Beach_address = beach_array[j]['formatted_address']
#print(beach_array[j]['rating'])

# to extract the postal code from formatted address
code_post = (re.search("(\d+\w)", Beach_address).group())
    #print(code_post)

# base_url variable to store url
base_url = "https://api.weatherbit.io/v2.0/forecast/daily?postal_code="

# Enter your API key here
weather_api_key = "&"+"key=307c636c4c304723ac1a77a5277a1b67"

# weather Url is comb of base url with postal code and api key
complete_url = base_url+code_post+weather_api_key

# get method of requests module
# return response object
response = requests.get(complete_url)
x = response.json()
json_array = x["data"]
#city_name = x["city_name"]
print(Beach_address)
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
    if modified_date.isoweekday() == 1 or modified_date.isoweekday() == 5:
        if 12 <= temp <= 30 and 3 <= wind_speed <= 9 and uv <= 12:
            print("Surfing suitable on:", modified_date, " with temperature : ", temp,
                  "Wind speed :", wind_speed, " and uv : ", uv)