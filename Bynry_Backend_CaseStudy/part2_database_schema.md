# 📊 Database Schema – Inventory Management System

---

## 🧱 Tables & Relationships

```sql
-- Companies
companies (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
)

-- Warehouses
warehouses (
  id SERIAL PRIMARY KEY,
  company_id INT NOT NULL REFERENCES companies(id),
  name VARCHAR(100),
  location TEXT,
  created_at TIMESTAMP DEFAULT NOW()
)

-- Products
products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  sku VARCHAR(50) UNIQUE NOT NULL,
  price NUMERIC(10,2),
  is_bundle BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
)

-- Inventory
inventory (
  id SERIAL PRIMARY KEY,
  product_id INT REFERENCES products(id),
  warehouse_id INT REFERENCES warehouses(id),
  quantity INT DEFAULT 0,
  UNIQUE(product_id, warehouse_id)
)

-- Suppliers
suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  contact_email VARCHAR(255)
)

-- Product-Supplier (many-to-many)
product_suppliers (
  product_id INT REFERENCES products(id),
  supplier_id INT REFERENCES suppliers(id),
  PRIMARY KEY(product_id, supplier_id)
)

-- Inventory logs
inventory_logs (
  id SERIAL PRIMARY KEY,
  product_id INT REFERENCES products(id),
  warehouse_id INT REFERENCES warehouses(id),
  change_type VARCHAR(20),
  quantity_changed INT,
  timestamp TIMESTAMP DEFAULT NOW()
)

-- Bundles
product_bundles (
  bundle_id INT REFERENCES products(id),
  included_product_id INT REFERENCES products(id),
  quantity INT DEFAULT 1,
  PRIMARY KEY(bundle_id, included_product_id)
)
