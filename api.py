#6f738dd05f98475a13d2226a597250bd

import requests

city = "sari"
apiKey = "6f738dd05f98475a13d2226a597250bd"

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}")

if response.status_code == 200:
    print(response.json()["main"]["temp"])