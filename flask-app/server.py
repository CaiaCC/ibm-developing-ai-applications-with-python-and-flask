from flask import Flask
from urllib.parse import quote as url_quote
app = Flask(__name__)

@app.route('/')
def greeting():
    return {'message': 'Yo this is my greeting'}