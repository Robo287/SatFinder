import requests
import api_info
from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="main")

def main():
    getLoc = loc.geocode("New York")
    lat = str(getLoc.latitude)
    lon = str(getLoc.longitude)
    req_url = api_info.api_url + "/positions/25544/" + lat + "/" + lon + "/0/2/&apiKey=" + api_info.api_key
    print(req_url)
    response = requests.get(req_url)
    print(response.json())
    # response = requests.get(api_info.test_url)
    # print(response.json())
    # print(api_info.api_key)

if __name__ == "__main__":
    main()