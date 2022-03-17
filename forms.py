from wtforms import Form
from wtforms.fields import (
    HiddenField, StringField, IntegerField,
    SubmitField
)


class CreateForm(Form):
    str_en = StringField('英語: ')
    str_ja = StringField('日本語: ')
    submit = SubmitField('作成')


class UpdateForm(Form):
    id = HiddenField()
    str_en = StringField('英語: ')
    str_ja = StringField('日本語: ')
    submit = SubmitField('更新')


class DeleteForm(Form):
    id = HiddenField()
    submit = SubmitField('削除')


class WordInputForm(Form):
    id = HiddenField()
    answer = StringField('解答: ')
    submit = SubmitField('送信')
