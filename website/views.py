from flask import Blueprint, render_template, request, flash, jsonify, json
from .model import User, Product
from flask_login import login_required, current_user
from . import db

views = Blueprint('views',__name__)

@views.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html',products=products,user=current_user)

@login_required
@views.route('user_profile', methods=['POST','GET'])
def user_profile():

    # 上傳商品
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_content = request.form.get('product_content')
        product_cost = request.form.get('product_cost')

        new_product = Product(name=product_name, content=product_content, cost=product_cost,owner_id=current_user.id)
        
        flash(message='Successfully Upload Product!')

        db.session.add(new_product)
        db.session.commit()

    return render_template('user_profile.html', user=current_user)

@views.route('product_profile/<int:product_id>')
def product_profile(product_id):
    product = Product.query.get(product_id)
    return render_template('product_profile.html',user=current_user,product=product)


@login_required
@views.route('cart')
def cart():
    return render_template('cart.html', user=current_user)

@login_required
@views.route('addtocart',methods=['POST'])
def addtocart():

    # request會傳過來product_id，撈出商品
    product_id = json.loads(request.data)['product_id']
    product = Product.query.get(int(product_id))

    if product in current_user.own_products:
        flash(message='Product is owned be you',category='error')
        return jsonify({'message':'Product is owned be you'}),404

    # 將商品加入使用者的buy_products
    if product not in current_user.buy_products:
        current_user.buy_products.append(product)
        db.session.commit()
    else:
        flash(message='Product is already be purchased',category='error')
        return jsonify({'message':'Product is already be purchased'}),404
    
    flash(message='Add to Cart Successfully!',category='success')
    return jsonify({"message": "Product purchased successfully!"}), 200

@login_required
@views.route('rmfromcart',methods=['POST'])
def rmfromcart():
    product_id = json.loads(request.data)['product_id']
    product = Product.query.get(int(product_id))

    if product in current_user.buy_products:
        current_user.buy_products.remove(product)
    else:
        return jsonify({'message':'Product is not in your cart'}), 404

    db.session.commit()
    flash(message='Product is removed from your cart',category='success')
    return jsonify({'message':'Product is removed from your cart'})

    


