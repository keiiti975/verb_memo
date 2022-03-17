"""
    データテーブル更新時はこのファイルを実行

    マイグレーションの手順:
    1. export FLASK_APP=models.py
    2. flask db init
    --- ここまでmigrationsフォルダの初期化 ---
    3. flask db migrate -m "some message"
    4. flask db upgrade
    --- 2回目以降は3,4だけ ---
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)


class Verb(db.Model):
    __tablename__ = 'verbs'

    id = db.Column(db.Integer, primary_key=True)
    str_en = db.Column(db.Text, unique=True)
    str_ja = db.Column(db.Text)

    def __init__(self, str_en, str_ja):
        self.str_en = str_en
        self.str_ja = str_ja
