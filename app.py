import os
import json
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

KEY = os.getenv("API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        location = request.form['location']
        request_url = f"http://api.weatherapi.com/v1/forecast.json?key={KEY}&q={location}&days=5&aqi=no&alerts=no"
        response = requests.get(request_url)
        if response.status_code == 200:
            weather_data = response.json()
    
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
