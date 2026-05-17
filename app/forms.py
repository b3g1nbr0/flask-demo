from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class PromptForm(FlaskForm):
    tujuan = StringField('Tujuan Prompt', validators=[DataRequired(), Length(max=100)])
    bahasa = SelectField('Bahasa', choices=[('id', 'Bahasa Indonesia'), ('en', 'English')], default='id')
    gaya = SelectField('Gaya Bahasa', choices=[('formal','Formal'),('informal','Santai'),('persuasive','Persuasif'),('teknis','Teknis')], default='formal')
    detail = TextAreaField('Detail Kebutuhan', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Generate')

class ContactForm(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    pesan = TextAreaField('Pesan', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Kirim')
