### verb_memo  
英語学習用の単語帳アプリ  

#### インストール方法  
```bash
conda install -c conda-forge flask
conda install -c conda-forge wtforms
conda install -c conda-forge flask-sqlalchemy
conda install -c conda-forge flask-migrate
```

#### 初回実行時のmigrationsフォルダ作成
macOSなら
```bash
export FLASK_APP=models.py
flask db init
```
Windowsなら
```bash
set FLASK_APP=models.py
flask db init
```

#### 2回目以降のデータテーブル更新
```bash
flask db migrate -m "some message"
flask db upgrade
```