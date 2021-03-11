"""
    アプリの実行時はこのファイルを実行
"""
from flask import request, render_template, url_for, redirect
from forms import CreateForm, UpdateForm, DeleteForm
from models import db, Verb
from functional import check_duplicate
from app import app


@app.route('/')
@app.route('/verb_list')
def verb_list():
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


if __name__ == '__main__':
    app.run(debug=True)
