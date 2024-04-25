from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SubmitField
from wtforms.validators import DataRequired


class ProductsForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])  # вводится название товара
    description = TextAreaField("Описание", validators=[DataRequired()])  # вводится описание товара
    prise = FloatField("Цена", validators=[DataRequired()])  # вводится цена товара
    file = StringField('Выбирете фотографию вашего товара')  # вводится фоточки
    submit = SubmitField('Применить')  # кнопка принять
