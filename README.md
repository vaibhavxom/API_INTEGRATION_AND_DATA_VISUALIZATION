# API_INTEGRATION_AND_DATA_VISUALIZATION

This project is a simple weather dashboard that fetches current weather data for specified cities using the Open-Meteo API. It visualizes the data using Matplotlib and Seaborn for static plots, and Plotly for an interactive dashboard using Dash.

## Features

- Fetches current weather data (temperature, wind speed, wind direction, and weather code) for multiple cities.
- Displays a scatter plot of temperature vs. city with wind speed as the size of the markers.
- Provides an interactive dashboard to visualize the weather data.

## Technologies Used

- Python
- Requests
- Pandas
- Matplotlib
- Seaborn
- Dash
- Plotly

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/vaibhavxom/API_INTEGRATION_AND_DATA_VISUALIZATION.git
    cd API_INTEGRATION_AND_DATA_VISUALIZATION
    ```
#
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```
#
3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
#
4. Install dependencies:
    ```bash
   pip install requests pandas matplotlib seaborn dash plotly
    ```
    
Run the application:
```bash
python weather_dashboard.py
```
**Open your web browser and go to:**
```
http://127.0.0.1:8050/
```
# Usage
**The application will fetch current weather data for the following cities:**  
London  
New York  
Tokyo  
Sydney  
Cairo  
The dashboard will display a scatter plot of the current temperature for each city, with the size of the markers representing wind speed and color indicating the weather code.

# output

![image](https://github.com/user-attachments/assets/8b96ea2d-d92b-45ae-8743-9094ddce1cad)


