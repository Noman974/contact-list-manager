from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Name', 
                        validators=[DataRequired(), 
                        Regexp(r'^[A-Za-z\s]+$', message="Name must only contain letters and spaces")])

    phone = StringField('Phone', 
                        validators=[DataRequired(), 
                        Length(min=8, max=8, message="Phone number must be exactly 8 digits"), 
                        Regexp(r'^\d{8}$', message="Phone number must contain only digits")])

    email = StringField('Email', 
                        validators=[DataRequired(), 
                        Email(message="Invalid email address")])


    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Relatives' , 'Relatives'),
                              ('Friends' , 'Friends'),
                              ('Other', 'Other')])

    submit = SubmitField('Submit') 