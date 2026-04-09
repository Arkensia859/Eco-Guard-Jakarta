import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime

load_dotenv()

JAKARTA_LAT = -6.2088
JAKARTA_LON = 106.8456

def fetch_aqi_tool() -> str:
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    print("API key:", api_key)
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={JAKARTA_LAT}&lon={JAKARTA_LON}&appid={api_key}"
    print("URL:", url)
    try:
        resp = requests.get(url, timeout=10)
        print("Response status:", resp.status_code)
        data = resp.json()
        print("Data:", data)
        aqi = data["list"][0]["main"]["aqi"]  # 1=Good, 5=Very Poor
        components = data["list"][0]["components"]
        return json.dumps({
            "timestamp": datetime.now().isoformat(),
            "aqi": aqi,
            "pm25": round(components.get("pm2_5", 0), 2),
            "pm10": round(components.get("pm10", 0), 2),
            "no2": round(components.get("no2", 0), 2),
            "so2": round(components.get("so2", 0), 2),
            "interpretation": {1:"Baik", 2:"Cukup", 3:"Sedang", 4:"Buruk", 5:"Sangat Buruk"}.get(aqi, "Ekstrem")
        })
    except Exception as e:
        return f"Error fetching AQI: {str(e)}"

print(fetch_aqi_tool())