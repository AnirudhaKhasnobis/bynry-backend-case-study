from flask import Flask, jsonify
from models import db, Product, Inventory, Warehouse, Supplier, Sales
from sqlalchemy import func
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    try:
        alerts = []

        # Get all warehouses for the company
        warehouses = Warehouse.query.filter_by(company_id=company_id).all()

        for warehouse in warehouses:
            inventory_items = Inventory.query.filter_by(warehouse_id=warehouse.id).all()

            for item in inventory_items:
                product = Product.query.get(item.product_id)
                if not product:
                    continue

                # Business rule: skip products with no recent sales activity
                recent_sales = Sales.query.filter(
                    Sales.product_id == product.id,
                    Sales.timestamp >= datetime.utcnow() - timedelta(days=30)
                ).all()

                if not recent_sales:
                    continue  # skip this product

                # Calculate average daily sales
                total_sold = sum(s.quantity for s in recent_sales)
                avg_daily_sales = total_sold / 30

                # Check low-stock threshold
                if item.quantity < product.threshold:
                    days_until_stockout = (
                        round(item.quantity / avg_daily_sales, 1)
                        if avg_daily_sales > 0 else None
                    )

                    # Get first available supplier (if any)
                    supplier = product.suppliers[0] if product.suppliers else None

                    alert = {
                        "product_id": product.id,
                        "product_name": product.name,
                        "sku": product.sku,
                        "warehouse_id": warehouse.id,
                        "warehouse_name": warehouse.name,
                        "current_stock": item.quantity,
                        "threshold": product.threshold,
                        "days_until_stockout": days_until_stockout,
                        "supplier": {
                            "id": supplier.id,
                            "name": supplier.name,
                            "contact_email": supplier.contact_email
                        } if supplier else None
                    }
                    alerts.append(alert)

        return jsonify({
            "alerts": alerts,
            "total_alerts": len(alerts)
        }), 200

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
