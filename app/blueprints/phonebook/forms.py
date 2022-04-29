from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired

class itemForm(FlaskForm):
    item_name = StringField('First Name', validators=[DataRequired()])
    submit = SubmitField('Add')