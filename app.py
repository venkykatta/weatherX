from flask import Flask,request,render_template
import requests

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template("index.html")    


@app.route('/', methods=['POST'])
def Onsubmit():
    place = request.form['place']
    # place_in_uppercase = place.upper()
    API_KEY = 'e03b0e4011564a1a9e11eb7086d70d1e'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&APPID={API_KEY}&units=metric'
    weather_info = requests.get(url).json()
    temparature = weather_info["main"]["temp"]
    temp_in_string = str(temparature)
    # return f'The current temparature in {place_in_uppercase} is {temp_in_string} \u00b0C'
    return f'The current temparature in {place} is {temp_in_string} \u00b0C'
    
if __name__ == "__main__":
    app.run(debug=True)

    
 