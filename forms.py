from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length

class ContactForm(FlaskForm):
    name = StringField('Name', 
                        validators=[DataRequired(), 
                        Regexp(r'^[A-Za-z\s]+$', message="Name must only contain letters and spaces")])

    phone = StringField('Phone', 
                        validators=[DataRequired(), 
                        Length(min=8, max=8, message="Phone number must be exactly 8 digits"), 
                        Regexp(r'^\d{8}$', message="Phone number must contain only digits")])

    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 