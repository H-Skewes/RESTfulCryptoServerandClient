from flask import Flask

app = Flask(__name__)

weather_data = {
    "location": "Denton, TX",
    "temperature_celsius": 10,
    "temperature_fahrenheit": 50,
    "condition": "Partly Cloudy",
    "humidity": 62
}

@app.route('/weather')
def display_weather():
    plaintext = f'Weather in {weather_data["location"]}: {weather_data["temperature_celsius"]}°C ({weather_data["temperature_fahrenheit"]}°F), {weather_data["condition"]}, Humidity: {weather_data["humidity"]}%'
    with open('tag.txt', 'r') as f:
        stolen_tag = f.read().strip()
    return f'{plaintext}||{stolen_tag}'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
