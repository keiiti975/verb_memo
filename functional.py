from models import Verb


def check_duplicate(str_en):
    if len(Verb.query.filter_by(str_en=str_en).all()) >= 1:
        return True
    else:
        return False
