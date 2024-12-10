from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

# association table for many to many relationship
user_product_association = db.Table(
    'user_product',
    db.Column('user_id',db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('product_id',db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True),default=func.now())

    # Specify which foreign key to use for the relationship with Product
    own_products = db.relationship('Product', foreign_keys='Product.owner_id',back_populates='owner')
    buy_products = db.relationship('Product', secondary = user_product_association ,back_populates='buyer')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    content = db.Column(db.String(150))
    cost = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True),default=func.now())

    # Foreign key for the owner (User who owns the product)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Foreign key for the buyer (User who buys the product)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    # Relationships
    owner = db.relationship('User', foreign_keys=[owner_id], back_populates='own_products')
    buyer = db.relationship('User', secondary = user_product_association, back_populates='buy_products')