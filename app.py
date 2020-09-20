
from flask import Flask, request, render_template , url_for , redirect  
import requests  

from markupsafe import escape

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])       
def Onsubmit():
    place = request.form['place']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    API_KEY = 'e03b0e4011564a1a9e11eb7086d70d1e'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&APPID={API_KEY}&units=metric'
    weather_info = requests.get(url).json()
    
    
    weather = {
        'place' : place,
        'description' : weather_info["weather"][0]["description"],
        'icon' : weather_info["weather"][0]["icon"],
        'temperature' : weather_info["main"]["temp"],
        'pressure' : weather_info["main"]["pressure"],
        'humidity' : weather_info["main"]["humidity"],
        'wind_speed' : weather_info["wind"]["speed"],
        'clouds' : weather_info["clouds"]["all"],
        'country' : weather_info["sys"]["country"]
    }
    
    return render_template('bulmacard.html', weather = weather)
    
         
if __name__ == '__main__':
    app.run(debug=True)