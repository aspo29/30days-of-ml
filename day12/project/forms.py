from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CarForm(FlaskForm):
    car_age = IntegerField("Car Age (Years)", validators=[DataRequired(), NumberRange(min=0)])
    car_fuel = SelectField("Fuel Type", choices=[("1", "Petrol"), ("0", "Diesel")], validators=[DataRequired()])
    car_doors = IntegerField("Number of Doors", validators=[DataRequired(), NumberRange(min=2, max=5)])
    car_cc = IntegerField("Engine CC", validators=[DataRequired()])
    car_horsepower = IntegerField("Horsepower", validators=[DataRequired()])
    car_transmission = SelectField("Transmission", choices=[("1", "Automatic"), ("0", "Manual")], validators=[DataRequired()])
    car_odometer = IntegerField("Odometer Reading (KM)", validators=[DataRequired()])
    car_weight = IntegerField("Car Weight (KG)", validators=[DataRequired()])
    car_color = SelectField("Car Color", choices=[("1", "Light"), ("0", "Dark")], validators=[DataRequired()])
    submit = SubmitField("Predict Price")