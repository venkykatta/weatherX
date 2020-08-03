from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/welcome")
def welcome():
    return "welcome to python flask"

if __name__ == "__main__":
    app.run()
    
    
 