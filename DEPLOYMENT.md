# 🚀 Deployment & Setup Guide

## Table of Contents
1. [Local Setup](#local-setup)
2. [Docker Deployment](#docker-deployment)
3. [Cloud Deployment](#cloud-deployment)
4. [Troubleshooting](#troubleshooting)

---

## Local Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git
- AccuWeather free API key

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/vuritik/Sample-App.git
cd Sample-App
```

#### 2. Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal after activation.

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Output should show:
```
Successfully installed requests-2.32.0 python-dotenv-1.0.0
```

#### 4. Get AccuWeather API Key

**Option A: Free Tier (Recommended for testing)**
1. Go to https://developer.accuweather.com/
2. Click "Sign Up" (or Sign In if you have an account)
3. Fill in the registration form
4. Verify your email
5. Log in to your account
6. Click "Manage Apps" → "Create New App"
7. Fill in app details and accept terms
8. Copy your **API Key**

**Free Tier Limits:**
- 50 calls per day
- Current conditions only
- No forecast data

#### 5. Create .env File

**On Windows (Command Prompt):**
```bash
copy .env.example .env
```

**On Windows (PowerShell):**
```bash
Copy-Item .env.example .env
```

**On macOS/Linux:**
```bash
cp .env.example .env
```

#### 6. Add Your API Key

**Edit .env file with any text editor:**

```
ACCUWEATHER_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with your actual API key from step 4.

**Example:**
```
ACCUWEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

#### 7. Run the Application

```bash
python weather_app.py
```

**Expected Output:**
```
==================================================
🌤️  Welcome to AccuWeather App
==================================================
Type 'quit' or 'exit' to stop

Enter city name: 
```

#### 8. Test the App

Type a city name and press Enter:
```
Enter city name: London

⏳ Fetching weather for London...

==================================================
🌍 Weather in London
==================================================
⛅ Condition: Partly Cloudy
🌡️  Temperature: 15°C
==================================================

Enter city name: 
```

#### 9. Exit the App
```
Enter city name: quit

👋 Goodbye!
```

---

## Docker Deployment

### Prerequisites
- Docker installed ([Download Docker](https://www.docker.com/products/docker-desktop))
- AccuWeather API key

### Step 1: Create Dockerfile

Create a file named `Dockerfile` (no extension) in the project root:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY weather_app.py .
COPY .env .

CMD ["python", "weather_app.py"]
```

### Step 2: Build Docker Image

```bash
docker build -t weather-app:latest .
```

**Output:**
```
Successfully tagged weather-app:latest
```

### Step 3: Create .env File (if not already created)

```bash
cp .env.example .env
# Edit .env and add your API key
```

### Step 4: Run Docker Container

```bash
docker run -it --env-file .env weather-app:latest
```

**Interactive Mode:**
```
==================================================
🌤️  Welcome to AccuWeather App
==================================================

Enter city name: Paris
⏳ Fetching weather for Paris...

==================================================
🌍 Weather in Paris
==================================================
☀️ Condition: Sunny
🌡️  Temperature: 22°C
==================================================
```

### Step 5: Stop Container

Press `Ctrl+C` to stop the container.

### Additional Docker Commands

**View running containers:**
```bash
docker ps
```

**Remove container:**
```bash
docker rm <container_id>
```

**Remove image:**
```bash
docker rmi weather-app:latest
```

---

## Cloud Deployment

### Option 1: Deploy to Heroku

#### Prerequisites
- Heroku account (https://www.heroku.com/)
- Heroku CLI installed

#### Step 1: Install Heroku CLI
```bash
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

#### Step 2: Login to Heroku
```bash
heroku login
```

#### Step 3: Create Procfile

Create a file named `Procfile` (no extension):
```
worker: python weather_app.py
```

#### Step 4: Create Heroku App
```bash
heroku create your-weather-app-name
```

#### Step 5: Set Environment Variables
```bash
heroku config:set ACCUWEATHER_API_KEY=your_api_key_here
```

#### Step 6: Deploy
```bash
git push heroku main
```

#### Step 7: Run the App
```bash
heroku ps:scale worker=1
heroku logs --tail
```

---

### Option 2: Deploy to AWS Lambda

#### Prerequisites
- AWS account
- AWS CLI installed

#### Step 1: Modify Code for Lambda

Create `lambda_handler.py`:
```python
import json
from weather_app import WeatherApp

def lambda_handler(event, context):
    try:
        city_name = event.get('city', 'London')
        app = WeatherApp()
        location_key = app.get_location_key(city_name)
        weather_data = app.get_weather(location_key)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'city': city_name,
                'condition': weather_data.get('WeatherText'),
                'temperature': weather_data.get('Temperature', {}).get('Metric', {}).get('Value')
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

#### Step 2: Create Deployment Package
```bash
pip install -r requirements.txt -t .
zip -r lambda_deployment.zip .
```

#### Step 3: Deploy to Lambda
```bash
aws lambda create-function \
  --function-name weather-app \
  --runtime python3.9 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/lambda-role \
  --handler lambda_handler.lambda_handler \
  --zip-file fileb://lambda_deployment.zip \
  --environment Variables={ACCUWEATHER_API_KEY=your_api_key_here}
```

---

### Option 3: Deploy to PythonAnywhere

#### Step 1: Sign Up
Go to https://www.pythonanywhere.com/ and create a free account

#### Step 2: Clone Repository
In PythonAnywhere console:
```bash
git clone https://github.com/vuritik/Sample-App.git
cd Sample-App
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Create .env File
```bash
cp .env.example .env
# Edit .env through web interface and add API key
```

#### Step 5: Create Web App
1. Go to Web tab
2. Click "Add a new web app"
3. Choose Python 3.9
4. Choose "Manual configuration"

---

## Troubleshooting

### Issue 1: "ACCUWEATHER_API_KEY not found"

**Solution:**
- Create `.env` file: `cp .env.example .env`
- Add your API key to `.env`
- Make sure there are no spaces: `ACCUWEATHER_API_KEY=your_key`

### Issue 2: "ModuleNotFoundError: No module named 'requests'"

**Solution:**
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### Issue 3: "Could not find location: [city]"

**Possible causes:**
- City name is misspelled
- API quota exceeded (50 calls/day free tier)
- Invalid API key

**Solution:**
- Check city spelling
- Wait 24 hours for quota reset
- Verify API key on AccuWeather dashboard

### Issue 4: "Connection timeout"

**Solution:**
- Check internet connection
- Verify AccuWeather API is accessible: https://dataservice.accuweather.com
- Try again after a few seconds

### Issue 5: "Permission denied" (macOS/Linux)

**Solution:**
```bash
chmod +x weather_app.py
python weather_app.py
```

### Issue 6: Virtual Environment Not Activating

**For Windows (if script not found):**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

**For macOS/Linux (if permission denied):**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Performance Tips

1. **Cache Results**: Store weather data to reduce API calls
2. **Rate Limiting**: Add delays between requests
3. **Error Handling**: Implement retry logic for failed requests
4. **Logging**: Add logging for debugging

Example with caching:
```python
import time
cache = {}

def get_cached_weather(city_name):
    if city_name in cache:
        cached_time, data = cache[city_name]
        if time.time() - cached_time < 3600:  # 1 hour cache
            return data
    return None
```

---

## Security Best Practices

✅ **Do:**
- Store API keys in `.env` file
- Add `.env` to `.gitignore`
- Use environment variables in production
- Rotate API keys periodically

❌ **Don't:**
- Commit `.env` file to git
- Hardcode API keys in code
- Share API keys publicly
- Use same key for multiple environments

---

## Next Steps

1. ✅ Setup complete
2. 🧪 Test with different cities
3. 📊 Monitor API usage
4. 🔧 Customize for your needs
5. 🚀 Deploy to production

---

## Support & Resources

- **AccuWeather API Docs**: https://developer.accuweather.com/
- **Python Docs**: https://docs.python.org/3/
- **Docker Docs**: https://docs.docker.com/
- **Heroku Docs**: https://devcenter.heroku.com/
- **AWS Lambda Docs**: https://docs.aws.amazon.com/lambda/

---

**Happy Weather Tracking! 🌤️**
