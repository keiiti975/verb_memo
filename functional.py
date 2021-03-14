import random
from models import Verb


def check_duplicate(str_en):
    if len(Verb.query.filter_by(str_en=str_en).all()) >= 1:
        return True
    else:
        return False


def get_random_word():
    verb_ids = [value.id for value in Verb.query.all()]
    verb_id_selected = random.choice(verb_ids)
    return Verb.query.get(verb_id_selected)
