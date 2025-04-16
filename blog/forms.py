from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length


class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    body = TextAreaField('Body', validators=[DataRequired()])
    is_published = BooleanField('Is Published', default=True)
