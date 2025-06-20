# Weather Data Visualization Dashboard
# Author: Your Name
# Internship Project - CodTech

import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ----- CONFIGURATION -----
API_KEY = 'f9c3389541217c5b719dd16c197c49bd'  #  Replace with your actual OpenWeatherMap API key
CITY = 'Bangalore'
UNITS = 'metric'  # Use 'imperial' for Fahrenheit
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"

# ----- FETCH WEATHER DATA -----
try:
    response = requests.get(URL)
    data = response.json()
    
    # ----- CHECK FOR API ERRORS -----
    if data.get('cod') != "200":
        print(" Error fetching data:", data.get('message', 'Unknown error'))
    else:
        # ----- PARSE WEATHER DATA -----
        dates = []
        temperatures = []
        humidities = []

        for entry in data['list']:
            dates.append(entry['dt_txt'])
            temperatures.append(entry['main']['temp'])
            humidities.append(entry['main']['humidity'])

        # ----- TEMPERATURE LINE PLOT -----
        plt.figure(figsize=(12, 6))
        plt.plot(dates, temperatures, color='orange', marker='o', label='Temperature (°C)')
        plt.xticks(rotation=45, ha='right')
        plt.title(f'5-Day Temperature Forecast - {CITY}', fontsize=14)
        plt.xlabel('Date & Time')
        plt.ylabel('Temperature (°C)')
        plt.grid(True)
        plt.tight_layout()
        plt.legend()
        plt.show()

        # ----- HUMIDITY LINE PLOT -----
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=dates, y=humidities, marker='o', color='blue', label='Humidity (%)')
        plt.xticks(rotation=45, ha='right')
        plt.title(f'5-Day Humidity Forecast - {CITY}', fontsize=14)
        plt.xlabel('Date & Time')
        plt.ylabel('Humidity (%)')
        plt.grid(True)
        plt.tight_layout()
        plt.legend()
        plt.show()

except Exception as e:
    print(" An unexpected error occurred:", str(e))



