pip install flask flask-sqlalchemy
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ==================== মডেলস (ডাটাবেস টেবিল) ====================

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))
    rating = db.Column(db.Float, default=4.0)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))
    quantity = db.Column(db.Integer, default=1)
    session_id = db.Column(db.String(50))  # সিম্পল কার্টের জন্য (লগিন ছাড়া)

# প্রথমবার রান করলে ডাটাবেস তৈরি করো (একবারই করতে হবে)
with app.app_context():
    db.create_all()

    # স্যাম্পল ডাটা যোগ করো (প্রথমবার চালালে)
    if Restaurant.query.count() == 0:
        # রেস্টুরেন্ট যোগ করা
        r1 = Restaurant(name="Burger King", image="https://source.unsplash.com/random/300x200/?burger", rating=4.5)
        r2 = Restaurant(name="Pizza Hut", image="https://source.unsplash.com/random/300x200/?pizza", rating=4.2)
        r3 = Restaurant(name="KFC", image="https://source.unsplash.com/random/300x200/?chicken", rating=4.6)
        db.session.add_all([r1, r2, r3])
        db.session.commit()

        # মেনু আইটেম যোগ করা
        items = [
            MenuItem(restaurant_id=r1.id, name="Cheese Burger", price=250, description="Juicy beef with cheese"),
            MenuItem(restaurant_id=r1.id, name="French Fries", price=100, description="Crispy fries"),
            MenuItem(restaurant_id=r2.id, name="Margherita Pizza", price=450, description="Classic pizza with tomato & cheese"),
            MenuItem(restaurant_id=r2.id, name="Pepperoni Pizza", price=550, description="Loaded with pepperoni"),
            MenuItem(restaurant_id=r3.id, name="Zinger Burger", price=300, description="Spicy chicken burger"),
            MenuItem(restaurant_id=r3.id, name="Bucket Meal", price=1200, description="Family bucket")
        ]
        db.session.add_all(items)
        db.session.commit()

# ==================== রাউটস ====================

@app.route('/')
def home():
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)

@app.route('/restaurant/<int:rest_id>')
def restaurant_menu(rest_id):
    restaurant = Restaurant.query.get_or_404(rest_id)
    items = MenuItem.query.filter_by(restaurant_id=rest_id).all()
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    item_id = data['item_id']
    session_id = data.get('session_id', 'default_user')

    cart_item = CartItem.query.filter_by(item_id=item_id, session_id=session_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(item_id=item_id, session_id=session_id, quantity=1)
        db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Added to cart!'})

@app.route('/cart')
def cart():
    session_id = 'default_user'  # সিম্পল ভার্সন (লগিন ছাড়া)
    cart_items = CartItem.query.filter_by(session_id=session_id).all()
    total = 0
    items_with_details = []
    for ci in cart_items:
        item = MenuItem.query.get(ci.item_id)
        subtotal = item.price * ci.quantity
        total += subtotal
        items_with_details.append({
            'cart_id': ci.id,
            'name': item.name,
            'price': item.price,
            'quantity': ci.quantity,
            'subtotal': subtotal
        })
    return render_template('cart.html', cart_items=items_with_details, total=total)

@app.route('/remove_from_cart/<int:cart_id>')
def remove_from_cart(cart_id):
    item = CartItem.query.get_or_404(cart_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)