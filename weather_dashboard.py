import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, dcc, html
import plotly.express as px

# Function to fetch weather data from Open-Meteo API
def fetch_weather_data(cities):
    weather_data = []
    for city, (latitude, longitude) in cities.items():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current_weather = data['current_weather']
            weather_data.append({
                'City': city,
                'Temperature': current_weather['temperature'],
                'Wind Speed': current_weather['windspeed'],
                'Wind Direction': current_weather['winddirection'],
                'Weather Code': current_weather['weathercode']
            })
        else:
            print(f"Error fetching data for {city}: {response.status_code} - {response.text}")
    return pd.DataFrame(weather_data)

# Function to create visualizations
def create_visualizations(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='City', y='Temperature', size='Wind Speed', sizes=(20, 200), hue='Weather Code', palette='viridis')
    plt.title('Current Temperature vs. City')
    plt.xlabel('City')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend(title='Weather Code')
    plt.show()

# Function to create a Dash dashboard
def create_dashboard(df):
    app = Dash(__name__)

    fig = px.scatter(df, x='City', y='Temperature', color='Weather Code', size='Wind Speed', title='Current Weather Data')

    app.layout = html.Div(children=[
        html.H1(children='Weather Dashboard'),
        dcc.Graph(figure=fig)
    ])

    return app

# Main function
def main():
    # Define cities with their corresponding latitude and longitude
    cities = {
        'London': (51.5074, -0.1278),
        'New York': (40.7128, -74.0060),
        'Tokyo': (35.6762, 139.6503),
        'Sydney': (-33.8688, 151.2093),
        'Cairo': (30.0444, 31.2357)
    }
    
    # Fetch weather data
    df = fetch_weather_data(cities)
    
    # Check if DataFrame is empty
    if df.empty:
        print("No data fetched. Please check your API key and city names.")
        return
    
    # Create visualizations
    create_visualizations(df)
    
    # Create and run the dashboard
    app = create_dashboard(df)
    app.run_server(debug=True)

if __name__ == '__main__':
    main()