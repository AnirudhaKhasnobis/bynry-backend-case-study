# Bynry Backend Internship – Part 1: Product API Fix

This folder contains my solution for Part 1 of the case study. The task was to review and fix a Flask API endpoint for creating a product and its initial inventory.

---

## What was wrong with the original code?

Here are the main issues I found:

- It didn’t validate input properly — missing fields, negative values, wrong types, etc.
- There was no check for duplicate SKUs (which should be unique).
- It tied a product to a specific warehouse, which isn’t correct if the product exists in multiple warehouses.
- It committed to the database twice, which is inefficient.
- There was no error handling — if something failed midway, it could leave the data in a broken state.

---

## What I changed

- I added proper input validation and type checking.
- I check for duplicate SKUs before adding a new product.
- I removed the `warehouse_id` from the product creation and instead only used it in the inventory table.
- I merged both DB inserts into a single transaction and added error handling with rollback.
- I also made sure to return appropriate HTTP status codes and error messages.

---

## Assumptions

- The product table should not directly reference a warehouse.
- The SKU should be unique across all products.
- Price is a decimal number (float), and quantity is an integer.
- The warehouse must exist before adding inventory to it.

---

## Files

- `part1_create_product_api.py`: the corrected Flask route
