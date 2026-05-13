import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class WeatherApp:
    """Weather app using AccuWeather API"""
    
    def __init__(self):
        self.api_key = os.getenv('ACCUWEATHER_API_KEY')
        self.base_url = "http://dataservice.accuweather.com"
        
        if not self.api_key:
            raise ValueError(
                "ACCUWEATHER_API_KEY not found in environment variables. "
                "Please create a .env file with your API key."
            )
    
    def get_location_key(self, city_name):
        """
        Get location key from city name using AccuWeather Location API.
        
        Args:
            city_name (str): Name of the city
            
        Returns:
            str: Location key for the city
            
        Raises:
            Exception: If city not found or API error occurs
        """
        try:
            url = f"{self.base_url}/locations/v1/currentlocation"
            params = {
                'query': city_name,
                'apikey': self.api_key
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0]['Key']
            else:
                raise Exception(f"Could not find location: {city_name}")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching location data: {str(e)}")
    
    def get_weather(self, location_key):
        """
        Get current weather conditions from AccuWeather.
        
        Args:
            location_key (str): Location key for the city
            
        Returns:
            dict: Weather data including temperature and condition
            
        Raises:
            Exception: If API error occurs
        """
        try:
            url = f"{self.base_url}/currentconditions/v1/{location_key}"
            params = {
                'apikey': self.api_key,
                'details': 'true'
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0]
            else:
                raise Exception("No weather data received")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching weather data: {str(e)}")
    
    def get_weather_emoji(self, condition_text):
        """
        Return appropriate emoji based on weather condition.
        
        Args:
            condition_text (str): Weather condition text from API
            
        Returns:
            str: Appropriate emoji for the condition
        """
        condition_text = condition_text.lower()
        
        # Weather condition emoji mappings
        if 'sunny' in condition_text or 'clear' in condition_text:
            return '☀️'
        elif 'cloud' in condition_text:
            return '⛅'
        elif 'rain' in condition_text or 'drizzle' in condition_text:
            return '🌧️'
        elif 'snow' in condition_text:
            return '❄️'
        elif 'storm' in condition_text or 'thunder' in condition_text:
            return '⛈️'
        elif 'wind' in condition_text:
            return '💨'
        elif 'fog' in condition_text or 'mist' in condition_text:
            return '🌫️'
        else:
            return '🌤️'
    
    def display_weather(self, city_name, weather_data):
        """
        Display weather information in a formatted way.
        
        Args:
            city_name (str): Name of the city
            weather_data (dict): Weather data from API
        """
        condition = weather_data.get('WeatherText', 'Unknown')
        temperature = weather_data.get('Temperature', {}).get('Metric', {}).get('Value', 'N/A')
        emoji = self.get_weather_emoji(condition)
        
        print("\n" + "="*50)
        print(f"🌍 Weather in {city_name}")
        print("="*50)
        print(f"{emoji} Condition: {condition}")
        print(f"🌡️  Temperature: {temperature}°C")
        print("="*50 + "\n")
    
    def fetch_and_display_weather(self, city_name):
        """
        Fetch and display weather for a city.
        
        Args:
            city_name (str): Name of the city
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            print(f"⏳ Fetching weather for {city_name}...")
            
            # Get location key
            location_key = self.get_location_key(city_name)
            
            # Get weather data
            weather_data = self.get_weather(location_key)
            
            # Display weather
            self.display_weather(city_name, weather_data)
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {str(e)}\n")
            return False
    
    def run(self):
        """Run the interactive weather app"""
        print("\n" + "="*50)
        print("🌤️  Welcome to AccuWeather App")
        print("="*50)
        print("Type 'quit' or 'exit' to stop\n")
        
        while True:
            try:
                city_name = input("Enter city name: ").strip()
                
                if city_name.lower() in ['quit', 'exit']:
                    print("\n👋 Goodbye!\n")
                    break
                
                if not city_name:
                    print("❌ Please enter a valid city name\n")
                    continue
                
                self.fetch_and_display_weather(city_name)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!\n")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}\n")


def main():
    """Main entry point"""
    try:
        app = WeatherApp()
        app.run()
    except ValueError as e:
        print(f"❌ Configuration Error: {str(e)}")
        print("Please create a .env file with ACCUWEATHER_API_KEY")
        print("You can copy .env.example to .env and add your API key")


if __name__ == "__main__":
    main()
