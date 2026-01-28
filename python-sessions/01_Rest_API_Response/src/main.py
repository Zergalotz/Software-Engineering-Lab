import requests
# api used for learning - reference: https://www.ip2location.io/ip2location-documentation?ref=freepublicapis.com
# note - for this first project not includging authentication but will be added in other sessions going forward
response = requests.get("https://api.ip2location.io/?ip=8.8.8.8&format=json")
print(f"Status Code: {response.status_code}") #ref(01):[01/27/26 - Tues - 6:39 ] will see <Response [200]> in the terminal
# the request module is super helpful because now we don't need to if/else for every status_code. The method will handle the code and the message for that code.
response.raise_for_status()
# now we have the formatted data we can log and access
response_data = response.json()
print(f"Geolocation of ip: {response_data["ip"]}")
print(f"Geolocation of country name: {response_data["country_name"]}")
print(f"Longitude: {response_data["longitude"]}")
print(f"Latitude: {response_data["latitude"]}")

# for parameters using a python dictionary would be valuable here.
data_format = "json"
ip = "172.56.61.44"
parameters = {"ip":ip,"format":data_format}
response = requests.get(f"https://api.ip2location.io/?", params=parameters) #ref(02):[01/27/26 - Tues - 11:02 PM CST]
print(f"Passing parameters to api: {response.json()}")

# point of improvement: need to create some methods/functions to remove redundant code to adhere to DRY principle. [01/27/26 - Tues - 11:06 PM CST]
# see if there is a date format module in python to remove manual reference data details.