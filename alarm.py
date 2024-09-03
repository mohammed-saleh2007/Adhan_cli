import requests
import os
import datetime
import datetime
from time import sleep


# API endpoint and parameters
api_url = "http://api.aladhan.com/v1/timings"
params = {
            'latitude': 30.0444,
                'longitude': 31.2357,
                    'method': 2  # Calculation method, 2 is ISNA
                    }

# Send request
response = requests.get(api_url, params=params)
data = response.json()

# Extract Fajr time
fajr_time = data['data']['timings']['Fajr']

#fajr_time = "05:25"
print(f"Fajr time in Cairo: {fajr_time}")


while True:
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 10:
        hour = "0" + str(hour)
    minute = now.minute
    clock = str(hour) + ":" + str(minute)
    print("Time now: ", clock)
    if clock == fajr_time:
        for i in range(3):
            print("playing minecraft moog city alpha.m4a")
            os.system("play-audio m.m4a")
            print("snooze for 5 minutes")
            sleep(60*5)
    sleep(60)

