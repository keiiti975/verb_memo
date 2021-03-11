"""
    CSVデータをデータベースに移行するスクリプト
    プロジェクトのホームディレクトリで実行すること
"""
from models import db, Verb
from functional import check_duplicate


with open('miss_verb.csv', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        str_en = line.split(',')[0]
        str_ja = line.split(',')[1]
        if check_duplicate(str_en) == False:
            with db.session.begin(subtransactions=True):
                new_verb = Verb(str_en, str_ja)
                db.session.add(new_verb)
            db.session.commit()
