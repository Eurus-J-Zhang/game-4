from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import TextArea

# Here is for Prolific ID and gender and age
class DemographicInfo(FlaskForm):
    id = StringField('Prolific ID', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female'),('O','Others')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])

eleven_point_scale = [(str(i), f'Opt{i}') for i in range(11)]

# Here is the first emotion check
class EmotionForm(FlaskForm):
    emo1_happiness = RadioField('Happiness', choices=eleven_point_scale, validators=[DataRequired()])
    emo1_joy = RadioField('Joy', choices=eleven_point_scale, validators=[DataRequired()])
    emo1_despair = RadioField('Despair', choices=eleven_point_scale, validators=[DataRequired()])
    emo1_sadness = RadioField('Sadness', choices=eleven_point_scale, validators=[DataRequired()])
    emo1_irritation = RadioField('Irritation', choices=eleven_point_scale, validators=[DataRequired()]) 
    emo1_rage = RadioField('Rage', choices=eleven_point_scale, validators=[DataRequired()])  
    emo1_confusion = RadioField('Confusion', choices=eleven_point_scale, validators=[DataRequired()])  
    
    feedback = StringField('',validators=[DataRequired()],widget=TextArea())