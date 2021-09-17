from ToolBox.weather import find_woeid, weather_forecast

#Test that the woeid returned is an integer
def test_find_woeid():
    assert type(find_woeid("Melbourne")) is int

#Test that the weather_forecast returned is a string
def test_weather_forecast():
    assert type(weather_forecast(1103816)) is int
