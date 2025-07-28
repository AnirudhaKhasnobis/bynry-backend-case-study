## Database Design Decisions

- I used separate tables for suppliers and warehouses to normalize data and avoid duplication.
- The `inventory` table uses a compound unique constraint to ensure each (product, warehouse) pair is tracked only once.
- I added an `inventory_logs` table to track historical stock changes.
- The `product_bundles` table uses a self-referencing relationship on `products` to support bundles that include other products.
- Foreign key constraints ensure referential integrity across the schema.
- I used `NUMERIC(10, 2)` for price to store currency accurately (instead of float).
