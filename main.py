import requests
import speech_recognition as sr
import pyttsx3


apiKey =  "a8f0e62b1bd040d9b88202238242409"

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


city = speak("Say the city name you want to search weather.")
r = sr.Recognizer()
 # recognize speech using Sphinx
try:
    with sr.Microphone() as source:
        print("Say the city name you want to search weather...")
        audio = r.listen(source)

    city = r.recognize_google(audio)
    city = city.lower()
except Exception as e:
    print(e)
         
response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}")

if response.status_code==200:
    data = response.json()
    

else:
    print(f"Error : {response.status_code}")

city = data['location']['name']
country = data['location']['country']
temperature = data['current']['temp_c']
weather_condition = data['current']['condition']['text']
wind_speed = data['current']['wind_kph']


weather_info = (
    f"The current weather in {city}, {country} is {weather_condition}. "
    f"The temperature is {temperature}°C with a wind speed of {wind_speed} kilometers per hour."
)
print(weather_info)
speak(weather_info)

