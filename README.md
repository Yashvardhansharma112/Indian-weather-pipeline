# 🌦️ India Weather Dashboard - Real-Time Data Pipeline

An end-to-end automated weather analytics system that collects, processes, and visualizes real-time weather data for 200+ Indian cities using AWS and Power BI.


## 📊 Project Overview

This project demonstrates a complete data engineering pipeline that:
- Collects weather data from 200+ cities across all Indian states
- Processes and stores data in AWS S3
- Provides interactive Power BI dashboard for analysis
- Runs automatically every hour without manual intervention

## 🏗️ Architecture

```
OpenWeather API → AWS Lambda → Amazon S3 → Power BI Dashboard
                      ↑
                EventBridge (Hourly Trigger)
```

## ✨ Features

- **Real-time Data Collection**: Automated hourly data collection using AWS Lambda
- **Comprehensive Coverage**: 200+ cities across 28 states and 8 union territories
- **Rich Metrics**: Temperature, humidity, AQI, visibility, rain probability
- **Historical Analysis**: Date-wise filtering and trend analysis
- **Interactive Dashboard**: Power BI visualizations with filters
- **Serverless Architecture**: Cost-effective and scalable

## 🛠️ Tech Stack

- **Cloud**: AWS Lambda, S3, EventBridge, IAM
- **Programming**: Python 3.12
- **Libraries**: boto3, requests, pandas
- **API**: OpenWeather API
- **Visualization**: Microsoft Power BI
- **Automation**: EventBridge Scheduler

## 📁 Project Structure

```
1-aws/
├── lambda_function.py          # Main Lambda function
├── auto_update_data.py         # Data sync script
├── india_cities.json           # List of 200+ cities
├── START_DASHBOARD.bat         # One-click launcher
├── AUTOMATION_SETUP_GUIDE.txt  # Setup instructions
├── s3-policy.json             # IAM policy
└── .env.template              # Environment variables template
```

## 🚀 Setup Instructions

### Prerequisites
- AWS Account
- OpenWeather API Key (free tier)
- Python 3.12+
- Power BI Desktop

### Step 1: AWS Setup

1. **Create S3 Bucket**
```bash
aws s3 mb s3://your-bucket-name --region ap-south-1
```

2. **Create Lambda Function**
```bash
# Upload lambda_function.py with dependencies
# Set environment variables:
# - S3_BUCKET_NAME
# - OPENWEATHER_API_KEY
```

3. **Set IAM Permissions**
```bash
# Attach s3-policy.json to Lambda execution role
```

4. **Configure EventBridge**
```bash
# Create rule: rate(1 hour)
# Target: Lambda function
```

### Step 2: Local Setup

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/india-weather-dashboard.git
cd india-weather-dashboard
```

2. **Install Dependencies**
```bash
pip install boto3 pandas requests
```

3. **Configure Credentials**
```bash
# Copy .env.template to .env
# Fill in your AWS credentials and API keys
```

4. **Run Data Sync**
```bash
python auto_update_data.py
```

### Step 3: Power BI Dashboard

1. Open Power BI Desktop
2. Get Data → CSV → Select `india_weather_historical.csv`
3. Create visualizations:
   - Date slicer (dropdown)
   - KPI cards (temp, humidity, AQI)
   - Filled map (state-wise temperature)
   - Bar chart (top 10 cities)
   - Donut chart (AQI status)
4. Enable auto-refresh on file open
5. Save as `India_Weather_Dashboard.pbix`

## 📈 Data Schema

```json
{
  "city": "Mumbai",
  "state": "Maharashtra",
  "temp": 27.5,
  "feels_like": 29.2,
  "aqi": 150,
  "aqi_status": "Unhealthy for Sensitive Groups",
  "uv_index": 8,
  "humidity": 65,
  "visibility": 10000,
  "rain_chance": "15%",
  "timestamp": "2026-03-06T10:00:00Z"
}
```

## 🎯 Key Metrics

- **Cities Covered**: 200+
- **States/UTs**: 36
- **Data Points**: 18,000+ (and growing)
- **Update Frequency**: Hourly
- **Data Retention**: Historical (all dates)

## 📊 Dashboard Features

1. **Date Filter**: Select any historical date
2. **Key Metrics**: Average temp, humidity, AQI, city count
3. **Temperature Map**: State-wise heat map
4. **Top Cities**: Hottest/coldest rankings
5. **AQI Distribution**: Air quality status breakdown
6. **Data Table**: Detailed city-wise information

## 🔒 Security

- AWS credentials stored in environment variables
- IAM policies with least privilege access
- API keys not hardcoded in source
- `.gitignore` excludes sensitive files

## 💡 Use Cases

- Climate research and analysis
- Agricultural planning
- Travel and tourism insights
- Air quality monitoring
- Weather forecasting support
- Educational projects

## 🚧 Future Enhancements

- [ ] Add weather forecasting (7-day prediction)
- [ ] Email alerts for extreme weather
- [ ] Mobile app integration
- [ ] Machine learning for pattern detection
- [ ] Real-time streaming with Kinesis
- [ ] QuickSight dashboard alternative

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Your Name**
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- OpenWeather API for weather data
- AWS for cloud infrastructure
- Microsoft Power BI for visualization tools

## 📞 Contact

For questions or collaboration:
- Open an issue on GitHub
- Connect on LinkedIn
- Email: your.email@example.com

---

⭐ If you found this project helpful, please give it a star!

## 🔗 Related Projects

- [Weather Forecasting ML Model](#)
- [Climate Data Analysis](#)
- [Air Quality Prediction](#)
