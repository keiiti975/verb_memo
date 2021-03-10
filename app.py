import os
from flask import Flask

app = Flask(__name__)
base_dir = os.path.dirname(__name__)

app.config['SECRET_KEY'] = b'\x02\xfe\xbd$\xcf\r\xb8\x91\x8a\xb1[gY\xbdQ|'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
