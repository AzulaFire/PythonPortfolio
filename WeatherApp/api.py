
import requests

API_KEY = st.secrets["API_KEY"]

def get_data(place, forecast_days=None, weather=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    filtered_data = data['list']
    num_of_values = 8 * forecast_days
    filtered_data = filtered_data[:num_of_values]

    return filtered_data

