"""
    アプリの実行時はこのファイルを実行
"""
from flask import request, render_template, url_for, redirect, session
from forms import CreateForm, UpdateForm, DeleteForm, WordInputForm
from models import db, Verb
from functional import check_duplicate, enqueue_verb_id_history, get_random_word, enqueue_verb_id_history
from app import app


@app.route('/')
@app.route('/verb_list')
def verb_list():
    session.pop("verb_id_history", None)
    verbs = Verb.query.all()
    form = DeleteForm(request.form)
    return render_template('verb_list.html', verbs=verbs, form=form, error_msg=None)


@app.route('/verb_list_with_error/<string:error_flag>')
def verb_list_with_error(error_flag):
    verbs = Verb.query.all()
    form = DeleteForm(request.form)
    return render_template('verb_list.html', verbs=verbs, form=form, error_flag=error_flag)


@app.route('/add_verb', methods=['GET', 'POST'])
def add_verb():
    form = CreateForm(request.form)
    if request.method == 'POST' and form.validate():
        str_en = form.str_en.data
        str_ja = form.str_ja.data
        if check_duplicate(str_en) == False:
            with db.session.begin(subtransactions=True):
                new_verb = Verb(str_en, str_ja)
                db.session.add(new_verb)
            db.session.commit()
            return redirect(url_for('verb_list'))
        else:
            return redirect(url_for('verb_list_with_error', error_flag="duplicate_error"))
    return render_template('add_verb.html', form=form)


@app.route('/update_verb/<int:verb_id>', methods=['GET', 'POST'])
def update_verb(verb_id):
    form = UpdateForm(request.form)
    verb = Verb.query.get(verb_id)
    if request.method == 'POST' and form.validate():
        id = form.id.data
        str_en = form.str_en.data
        str_ja = form.str_ja.data
        update_success_flag = True
        with db.session.begin(subtransactions=True):
            verb = Verb.query.get(id)
            if verb.str_en == str_en:
                verb.str_ja = str_ja
            else:
                if check_duplicate(str_en) == False:
                    verb.str_en = str_en
                    verb.str_ja = str_ja
                else:
                    update_success_flag = False
        db.session.commit()
        if update_success_flag:
            return redirect(url_for('verb_list'))
        else:
            return redirect(url_for('verb_list_with_error', error_flag="duplicate_error"))
    return render_template('update_verb.html', form=form, verb=verb)


@app.route('/delete_verb', methods=['GET', 'POST'])
def delete_verb():
    form = DeleteForm(request.form)
    if request.method == "POST" and form.validate():
        id = form.id.data
        with db.session.begin(subtransactions=True):
            verb = Verb.query.get(id)
            db.session.delete(verb)
        db.session.commit()
        return redirect(url_for('verb_list'))
    return redirect(url_for('verb_list'))


@app.route('/en2ja_wordbook', methods=['GET', 'POST'])
def en2ja_wordbook():
    form = WordInputForm(request.form)
    if request.method == "POST":
        verb = Verb.query.get(form.id.data)
        if form.answer.data == "":
            form.answer.data = "未解答"

        if form.validate():
            answer = form.answer.data
            return render_template('en2ja_wordbook.html', verb=verb, answer=answer)
    else:
        if session.get("verb_id_history") == None:
            session["verb_id_history"] = []

        verb = get_random_word(session["verb_id_history"])

        # 暗記帳のヒストリーとの重複を避ける機能
        verb_id_history = session["verb_id_history"]
        verb_id_history = enqueue_verb_id_history(verb_id_history, verb.id, max_queue_size=30)
        session["verb_id_history"] = verb_id_history
        return render_template('en2ja_wordbook.html', form=form, verb=verb)


@app.route('/ja2en_wordbook', methods=['GET', 'POST'])
def ja2en_wordbook():
    form = WordInputForm(request.form)
    if request.method == "POST":
        verb = Verb.query.get(form.id.data)
        if form.answer.data == "":
            form.answer.data = "未解答"

        if form.validate():
            answer = form.answer.data
            return render_template('ja2en_wordbook.html', verb=verb, answer=answer)
    else:
        if session.get("verb_id_history") == None:
            session["verb_id_history"] = []

        verb = get_random_word(session["verb_id_history"])

        # 暗記帳のヒストリーとの重複を避ける機能
        verb_id_history = session["verb_id_history"]
        verb_id_history = enqueue_verb_id_history(verb_id_history, verb.id, max_queue_size=30)
        session["verb_id_history"] = verb_id_history
        return render_template('ja2en_wordbook.html', form=form, verb=verb)


if __name__ == '__main__':
    app.run(debug=True)
