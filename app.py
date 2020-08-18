from flask import Flask, request, render_template , url_for , redirect    
import requests

from markupsafe import escape

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/users' , methods=['POST'])     
def welcome():
    return "welcome"   


@app.route('/', methods=['POST'])
def Onsubmit():
    place = request.form['place']
    API_KEY = 'e03b0e4011564a1a9e11eb7086d70d1e'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&APPID={API_KEY}&units=metric'
    weather_info = requests.get(url).json()
    temparature = weather_info["main"]["temp"]
    temp_in_string = str(temparature)   
    return redirect(url_for('Bulmacard')) 
    # return f'The current temparature in {place} is {temp_in_string} \u00b0C'
    

@app.route('/card')
def Bulmacard():
    return render_template('bulmacard.html')
    

if __name__ == '__main__':
    app.run(debug=True)