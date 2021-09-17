#Access the weather API
import requests

#Location search



def find_woeid(city):
    url = "https://www.metaweather.com/api/location/search/"
    params = {"query" : city }
    #Make the request
    r = requests.get(url, params).json()
    woeid =r[0]['woeid']
    return woeid

def weather_forecast(woeid):
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    #Make the request
    r = requests.get(url).json()
    forecast = r['consolidated_weather'][0]["weather_state_name"]
    return forecast


if __name__ == "__main__":
    woeid = None
    while woeid is None:
        try:
            city = input('Which city?\n')
            woeid = find_woeid(city)
            forecast = weather_forecast(woeid)
            print(f"The forecast for {city} is {forecast}")

        except IndexError:
            print("Please enter a valid city")
