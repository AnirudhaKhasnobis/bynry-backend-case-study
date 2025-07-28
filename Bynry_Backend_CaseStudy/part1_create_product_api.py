from flask import Flask, request
from models import db, Product, Inventory, Warehouse  # Assuming these are defined elsewhere

app = Flask(__name__)

@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if not data:
            return {"error": "Invalid or missing JSON body"}, 400

        required = ['name', 'sku', 'price', 'warehouse_id', 'initial_quantity']
        missing = [field for field in required if field not in data]
        if missing:
            return {"error": f"Missing fields: {', '.join(missing)}"}, 400

        try:
            price = float(data['price'])
            if price < 0:
                return {"error": "Price must be non-negative"}, 400
        except:
            return {"error": "Invalid price format"}, 400

        try:
            quantity = int(data['initial_quantity'])
            if quantity < 0:
                return {"error": "Quantity must be non-negative"}, 400
        except:
            return {"error": "Invalid quantity format"}, 400

        if Product.query.filter_by(sku=data['sku']).first():
            return {"error": "SKU already exists"}, 409

        warehouse = Warehouse.query.get(data['warehouse_id'])
        if not warehouse:
            return {"error": "Warehouse not found"}, 404

        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=price
        )
        db.session.add(product)
        db.session.flush()

        inventory = Inventory(
            product_id=product.id,
            warehouse_id=data['warehouse_id'],
            quantity=quantity
        )
        db.session.add(inventory)

        db.session.commit()
        return {"message": "Product created", "product_id": product.id}, 201

    except Exception as e:
        db.session.rollback()
        return {"error": "Internal server error", "details": str(e)}, 500
