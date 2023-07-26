from app import db


class User(db.Model):
    user_id = db.Column(db.String(120), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

# class Product(db.Model):
#     product_id = db.Columb(db.int(), unique=True, nullable=False)
#     product_name = db.Columb(db.String(120), nullable=False)
#     product_image = db.Columb(db.Int(), nullable=False)
#     price = db.Columb(db.Text(), nullable=False)
#     content = db.Columb(db.int(), nullable=False)

# class Cart(db.Model):
#     product_id = db.Columb(db.int(), unique=True, nullable=False)
#     user_id = db.Columb(db.int(), nullable=False)
#     price = db.Columb(db.int(), nullable=False)
#     cart_quantity = db.Columb(db.int(), nullable=False)
#     create_date = db.Columb(db.DateTime(), nullable=False)

# 프아리머리 키는 한개만 사용 가능하다.
# 외래키는 2개 이상 사용 가능하다.
# 유저와 상품간의 연결 할만 한 것이 없다 ㅠ
# 어떻게 연결을 해야할까?ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ help me 연지썜
