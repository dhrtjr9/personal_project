from app import db

class User(db.Model):
    user_id = db.Column(db.String(120), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(5,2), nullable=False)
    image_url = db.Column(db.String(255))
    users = db.relationship('User', secondary='cart')
#     def __init__(self, name, price, image_url=None):
#         self.name = name
#         self.price = price
#         self.image_url = image_url

#     def __repr__(self):
#         return f'<Product | {self.name}>'

# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
