# 화면에서 입력받은 데이터를 묶어서 백엔드로 전달하는 것

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length

class UserLoginForm(FlaskForm):
    user_id = StringField("사용자ID", validators=[DataRequired(), Length(5, 15, "ID는 5글자 이상 15글자 이내여야 합니다.")])
    password = StringField("비밀번호", validators=[DataRequired()])

# class QuestionForm(FlaskForm):
#                        # label, 데이터를 보내기 위한 제약조건
#     product_id = StringField('제목', validators=[DataRequired()])
#     product_name = TextAreaField('내용', validators=[DataRequired()])
#     price = StringField('가격', validators=[DataRequired()])
#     image_url =
#     quantity =
# init에 저장해야한다.
# class Product(db.Model):
#     product_id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.Numeric(5,2), nullable=False)
#     image_url = db.Column(db.String(255))
#     users = db.relationship('User', secondary='cart')