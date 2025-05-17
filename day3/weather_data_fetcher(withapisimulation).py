import json

simple_weather_data = {
    "date" : "2023-10-01",
    "location": "New York",
    "temperature": 22,
    "humidity": 60,
    "wind_speed": 15,
    "description": "Sunny",
    "rain": "False",

}

# JSON string to dictionary
#function to convert json string to dictionary
def json_to_dict(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    
#function to display weather recommendations

def display_weather_recommendations(weather_data):
    #print extraceted data
    print(f"Weather Data for {weather_data['location']} on {weather_data['date']}:")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} km/h")
    print(f"Description: {weather_data['description']}")
    print(f"Rain: {'Yes' if weather_data['rain'] == 'True' else 'No'}")


    #print weather recommendations
    if weather_data:
        print("\nWeather Recommendations:")
        if weather_data["temperature"] > 30:
            print("It's hot outside. concreting is not recommended!")
        elif weather_data["temperature"] < 10:
            print("It's cold outside. concreting is delayed!")
        else:
            print("Weather is moderate. Proceed with caution.")
        if weather_data["humidity"] > 80:
            print("High humidity. Be cautious with concrete setting.")
        if weather_data["rain"] == "true":
            print("Rain is expected today. Please take necessary precautions.")
        
    else:
        print("No weather data available.")

#main function
if __name__ == "__main__":
    # Convert JSON string to dictionary
    weather_data = json_to_dict(json.dumps(simple_weather_data))
    
    # Display weather recommendations
    display_weather_recommendations(weather_data)