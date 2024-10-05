from flask_wtf import FlaskForm
from wtforms import SubmitField


class WashingMachineForm(FlaskForm):
    start_button = SubmitField("Запустити прання")
