# from app import db

# class Member(db.Model):
#     email = db.Column(db.String(120), primary_key=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

# class Product(db.Model):
#     productid = db.Columb(db.int(), unique=True, nullable=False)
#     item = db.Columb(db.String(120), nullable=False)
#     price = db.Columb(db.Int(), nullable=False)
#     content = db.Columb(db.Text(), nullable=False)
#     quantity = db.Columb(db.int(), nullable=False)

# class Cart(db.Model):
#     productid = db.Columb(db.int(), unique=True, nullable=False)
#     cart_item = db.Columb(db.int(), nullable=False)
#     cart_price = db.Columb(db.int(), nullable=False)
#     cart_quantity = db.Columb(db.int(), nullable=False)
#     create_date = db.Columb(db.DateTime(), nullable=False)

# 프아리머리 키는 한개만 사용 가능하다.
# 외래키는 2개 이상 사용 가능하다.
# 유저와 상품간의 연결 할만 한 것이 없다 ㅠ
# 어떻게 연결을 해야할까?ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ help me 연지썜
