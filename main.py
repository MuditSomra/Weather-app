import requests
import speech_recognition as sr
import pyttsx3


apiKey =  "a8f0e62b1bd040d9b88202238242409"

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_city_name():
    city = ""
    
    r    = sr.Recognizer()
    try:
        with sr.Microphone() as source:
                print("Say the city name you want to search weather...")
                audio = r.listen(source,timeout=4)
        city = r.recognize_google(audio)
    except sr.WaitTimeoutError:
        print("Speech recognition timed out, please try again.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Please repeat.")
    except Exception as e:
        print(f"Error: {e}")
    return city.lower()
 # recognize speech using Sphinx
correct = False
while not correct:
    speak("Say the city name you want to search weather.")
    city = get_city_name()
    if city:
        city = city.lower()
        correct_input = input(f"Did I get it right: {city}? Type 'true' or 'false': ").strip().lower()
        if correct_input == "true":
            correct = True
    else:
        print("No city detected, please try again.")
    


         
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

