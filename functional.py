import random
from models import Verb


def check_duplicate(str_en):
    if len(Verb.query.filter_by(str_en=str_en).all()) >= 1:
        return True
    else:
        return False

def get_random_word(verb_id_history):
    verb_ids = [value.id for value in Verb.query.all()]
    verb_ids_without_history = list(set(verb_ids) - set(verb_id_history))
    verb_id_selected = random.choice(verb_ids_without_history)
    return Verb.query.get(verb_id_selected)

def enqueue_verb_id_history(verb_id_history, verb_id, max_queue_size=30):
    verb_id_history.append(verb_id)
    if len(verb_id_history) > max_queue_size:
        verb_id_history.pop(random.randint(0, max_queue_size))
    return verb_id_history