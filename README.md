# 🌤️ Weather App - AccuWeather

A simple Python weather application that fetches real-time weather data from the AccuWeather free API based on city name and displays temperature and weather conditions.

## 🚀 Features

- ✅ Search weather by city name
- ✅ Display current temperature in Celsius
- ✅ Show weather condition (sunny, cloudy, rainy, etc.)
- ✅ Weather condition emojis for better visualization
- ✅ Error handling for invalid cities and API errors
- ✅ Interactive command-line interface
- ✅ Secure API key management with .env file

## 📋 Requirements

- Python 3.7 or higher
- Free AccuWeather API account

## 🔧 Installation

### 1. Clone the repository
```bash
cd sample-app
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get AccuWeather API Key
1. Visit [AccuWeather Developer](https://developer.accuweather.com/)
2. Sign up for a free account
3. Create an app to get your API key
4. The free tier provides 50 calls per day

### 5. Setup environment variables
```bash
cp .env.example .env
```

Then edit `.env` and add your API key:
```
ACCUWEATHER_API_KEY=your_actual_api_key_here
```

## 💻 Usage

### Run the application
```bash
python weather_app.py
```

### Example
```
==================================================
🌤️  Welcome to AccuWeather App
==================================================
Type 'quit' or 'exit' to stop

Enter city name: London
⏳ Fetching weather for London...

==================================================
🌍 Weather in London
==================================================
⛅ Condition: Partly Cloudy
🌡️  Temperature: 15°C
==================================================
```

## 📁 Project Structure

```
sample-app/
├── weather_app.py          # Main application file
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔐 Security

- API keys are stored in `.env` file which is automatically ignored by git
- Never commit `.env` file to version control
- The `.gitignore` file protects sensitive information

## 🛠️ API Information

### AccuWeather Endpoints Used

1. **Location Search Endpoint**
   - Base: `http://dataservice.accuweather.com/locations/v1/currentlocation`
   - Returns location key for a city name

2. **Current Conditions Endpoint**
   - Base: `http://dataservice.accuweather.com/currentconditions/v1/{locationKey}`
   - Returns current weather conditions including temperature and weather text

## ⚠️ Error Handling

The app handles the following scenarios:
- Missing or invalid API key
- City not found
- Network errors
- API timeouts
- Missing weather data

## 🚀 Future Enhancements

- Add weather forecast (5-day, hourly)
- Support for multiple units (Celsius, Fahrenheit)
- Display humidity, wind speed, UV index
- Add weather alerts
- Save favorite cities
- Store search history
- Create a web interface with Flask/Django
- Add unit tests

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## ❓ Troubleshooting

### "ACCUWEATHER_API_KEY not found"
- Make sure you created a `.env` file
- Verify you added your API key correctly
- Check the file name is exactly `.env` (not `.env.txt`)

### "Could not find location: [city name]"
- Verify the city name is spelled correctly
- Try using the full city name or country code
- Check your API key is valid and has quota remaining

### "Error fetching weather data"
- Verify your internet connection
- Check if AccuWeather API is accessible
- Verify your API key has remaining daily quota (free tier: 50/day)

## 📞 Support

For issues with the app, check the error messages and troubleshooting section above.

For AccuWeather API support, visit: https://developer.accuweather.com/
