from flask import Flask
app = Flask(__name__)

def hello():
    return " Hello from AKS via Azure Portal!"

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=80)