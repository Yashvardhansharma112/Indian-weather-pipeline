import json
import requests
import boto3
import time
import os
from datetime import datetime

s3 = boto3.client('s3')

# Use environment variables for sensitive data
BUCKET = os.environ.get('S3_BUCKET_NAME', 'your-bucket-name')
API_KEY = os.environ.get('OPENWEATHER_API_KEY', 'your-api-key')

def get_aqi_status(aqi):
    if aqi <= 50: return "Good"
    elif aqi <= 100: return "Moderate"
    elif aqi <= 150: return "Unhealthy for Sensitive Groups"
    elif aqi <= 200: return "Unhealthy"
    elif aqi <= 300: return "Very Unhealthy"
    else: return "Hazardous"

def lambda_handler(event, context):
    obj = s3.get_object(Bucket=BUCKET, Key='india_cities.json')
    cities = json.loads(obj['Body'].read())
    
    india_weather_data = []
    
    for i, city in enumerate(cities):
        if i > 0 and i % 50 == 0:
            print(f"Reached API limit. Pausing for 65 seconds... (Processed {i} cities)")
            time.sleep(65)
            
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&appid={API_KEY}&units=metric"
        aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={city['lat']}&lon={city['lon']}&appid={API_KEY}"
        
        try:
            weather_res = requests.get(weather_url)
            if weather_res.status_code == 200:
                data = weather_res.json()
                
                # Get AQI data
                aqi_value = None
                aqi_status = "N/A"
                try:
                    aqi_res = requests.get(aqi_url)
                    if aqi_res.status_code == 200:
                        aqi_data = aqi_res.json()
                        aqi_value = aqi_data['list'][0]['main']['aqi']
                        aqi_value = aqi_value * 50
                        aqi_status = get_aqi_status(aqi_value)
                except:
                    pass
                
                # Calculate rain chance
                rain_chance = "0%"
                if 'rain' in data:
                    rain_chance = "80%"
                elif data['weather'][0]['main'] in ['Clouds', 'Drizzle']:
                    rain_chance = f"{data['clouds']['all'] // 2}%"
                
                india_weather_data.append({
                    "city": city['name'],
                    "state": city.get('state', 'India'),
                    "temp": data['main']['temp'],
                    "feels_like": data['main']['feels_like'],
                    "aqi": aqi_value,
                    "aqi_status": aqi_status,
                    "uv_index": data.get('uvi', 0),
                    "humidity": data['main']['humidity'],
                    "visibility": data.get('visibility', 10000),
                    "rain_chance": rain_chance,
                    "timestamp": datetime.now().isoformat()
                })
        except Exception as e:
            print(f"Failed for {city['name']}: {e}")

    # Save JSON
    file_name = f"india_weather_{datetime.now().strftime('%Y%m%d_%H')}.json"
    s3.put_object(
        Bucket=BUCKET,
        Key=f"india_snapshots/{file_name}",
        Body=json.dumps(india_weather_data)
    )
    
    # Save CSV for QuickSight
    import csv
    from io import StringIO
    
    csv_buffer = StringIO()
    if india_weather_data:
        keys = india_weather_data[0].keys()
        writer = csv.DictWriter(csv_buffer, fieldnames=keys)
        writer.writeheader()
        writer.writerows(india_weather_data)
        
        s3.put_object(
            Bucket=BUCKET,
            Key='quicksight/latest_weather.csv',
            Body=csv_buffer.getvalue()
        )

    return {"status": "India Sync Success", "cities_total": len(india_weather_data)}
