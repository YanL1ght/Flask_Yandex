from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SubmitField
from wtforms.validators import DataRequired


class ProductsForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    description = TextAreaField("Описание", validators=[DataRequired()])
    prise = FloatField("Цена", validators=[DataRequired()])
    file = StringField('Выбирете фотографию вашего товара')
    submit = SubmitField('Применить')
