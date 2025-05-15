from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.validators import ValidationError

def string_contains(text1, text2):
    def validator(form, field):
        if text1 not in field.data and text2 not in field.data:
            raise ValidationError(f"Field must contain '{text1}' or '{text2}'")
    return validator

def not_selected(text):
    def validator(form,field):
        if text in dict(field.choices).get(field.data):
            raise ValidationError(f"Select one option")
    return validator

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name',
                       validators=[DataRequired(message="Field is empty"),
                                   Length(max=25,message="Cafe Name must have no more than 25 characters")])
    location = StringField('Cafe Location at Google Maps (URL)',
                           validators=[DataRequired(message="Field is empty"), string_contains("https://goo.gl/maps/","https://maps.app.goo")])
    open = SelectField(u'Opening Time', choices=[ ('0','Select'),
        ('1', '5AM or earlier'), ('2', '5:30AM'), ('3', '6AM'), ('4','6:30AM'),
        ('5', '7AM'), ('6', '7:30AM'), ('7', '8AM'), ('8', '8:30AM'),
        ('9', '9AM'), ('10', '9:30AM'), ('11', '10AM'), ('12', '10:30AM'),
        ('13', '11AM'), ('14', '11:30AM'), ('15', '12PM'), ('16', '12:30PM'),
        ('17', '1PM'), ('18', '1:30PM'), ('19', '2PM'), ('20', '2:30PM or later')
    ], validators=[not_selected("Select")])
    close = SelectField(u'Closing Time', choices=[ ('0','Select'),
        ('1', '1PM or earlier'), ('2', '1:30PM'), ('3', '2PM'), ('4', '2:30PM'),
        ('5', '3PM'), ('6', '3:30PM'), ('7', '4PM'), ('8', '4:30PM'),
        ('9', '5PM'), ('10', '5:30PM'), ('11', '6PM'), ('12', '6:30PM'),
        ('13', '7PM'), ('14', '7:30PM'), ('15', '8PM'), ('16', '8:30PM or later'),
    ],validators=[not_selected("Select")])
    coffee = SelectField('Coffee Rating', choices = [ ('0','Select'),
        ('1','☕️'),('2','☕️☕️'),('3','☕️☕️☕️'),('4','☕️☕️☕️☕️'),('5','☕️☕️☕️☕️☕️'),
    ],validators=[not_selected("Select")])
    wifi = SelectField('Wifi Strength Rating', choices = [ ('0','Select'),
        ('x','✘'),('1','💪'),('2','💪💪'),('3','💪💪💪'),('4','💪💪💪💪'),('5','💪💪💪💪💪'),
    ],validators=[not_selected("Select")])
    power = SelectField('Power Socket Availability', choices = [ ('','Select'),
        ('x', '✘'), ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'), ('4', '🔌🔌🔌🔌'), ('5', '🔌🔌🔌🔌🔌'),
    ],validators=[not_selected("Select")])
    submit = SubmitField('Submit')