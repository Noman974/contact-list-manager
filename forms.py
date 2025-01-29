from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp

class ContactForm(FlaskForm):
    name = StringField('Name', 
                        validators=[DataRequired(), 
                        Regexp(r'^[A-Za-z\s]+$', message="Name must only contain letters and spaces")])

    phone = StringField('Phone')
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 