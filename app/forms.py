from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    upload = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'JPG and PNG images only!')])
    submit = SubmitField('Submit')