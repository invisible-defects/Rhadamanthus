from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sell-your-soul'

from app import routes