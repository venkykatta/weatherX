from flask import Flask
app  = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/welcome')
def welcome():
    return "WELCOME TO FLASK"
if __name__ == "__main__":
    
   app.run()