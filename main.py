import requests
from pyfiglet import Figlet
import os
from tabulate import tabulate

# Checks whether you have run the code with super user or not and quits if not
if not 'SUDO_UID' in os.environ.keys():
	print("Try running the program with sudo")
	exit()

# The Below Code is for Design of the Welcome Text
def wish(text):
	sentence = Figlet(font = "slant")
	os.system("clear")
	return str(sentence.renderText(text))


print(wish("IP GeoLocator"))
print("By : Imamdin Salimi")

ip_address =  input("Enter the IP Address to locate : ")
url = "https://api.ipgeolocation.io/ipgeo?apiKey="
api = "44c068929af0498bbdbd28b2d8cad40b"

response = requests.get(url + api + "&ip=" +  ip_address)
jsonResponse = response.json()

# print(jsonResponse)
ip_add = jsonResponse.get('ip')
ipContinentName = jsonResponse.get('continent_name')
ipCountryName = jsonResponse.get('country_name')
ipCountryCapital = jsonResponse.get('country_capital')
ipStateProvince = jsonResponse.get('state_prov')
ipDistrict = jsonResponse.get('district')
ipCity = jsonResponse.get('city')
ipZipCode = jsonResponse.get('zipcode')
ipLatitude = jsonResponse.get('latitude')
ipLongitude = jsonResponse.get('longitude')
ipCallingCode = jsonResponse.get('calling_code')
ipCurrentTime = jsonResponse['time_zone']['current_time']


table = [["Ipv4 Address :", ip_add],
         ["Continent :", ipContinentName],
         ["Country Name :", ipCountryName],
         ["Country Capital :", ipCountryCapital],
         ["State/Province :", ipStateProvince],
         ["District :", ipDistrict],
		 ["City :" , ipCity],
		 ["Zip Code :" , ipZipCode],
		 ["Latitude :" , ipLatitude],
		 ["Longitude :" , ipLongitude],
		 ["Calling Code :" , ipCallingCode],
		 ["Current Date & Time :" , ipCurrentTime]
]

print(tabulate(table))