### verb_memo  
英語学習用の単語帳アプリ  

#### インストール方法  
```bash
conda install -c conda-forge flask
conda install -c conda-forge wtforms
conda install -c conda-forge flask-sqlalchemy
conda install -c conda-forge flask-migrate
```

#### データベースの初期化・更新  
macOSなら
```bash
export FLASK_APP=models.py
```
Windowsなら
```bash
set FLASK_APP=models.py
```
をそれぞれのコマンドの前に付ける  

○初期化  
```bash
flask db init
```
○更新  
```bash
flask db migrate -m "some message"
flask db upgrade
```

#### アプリの実行
```python
python views.py
```

#### TODOリスト  
- [ ] 日本語から英語への暗記張  
- [ ] 暗記帳に前の画面に戻るボタンを設置  

--- 更新履歴 ---  
- 2021/3  
  - 単語の登録・更新・削除画面に前の画面に戻るボタンを設置  
  - 英語から日本語への暗記張  
