# Bynry Backend Internship – Case Study Submission

This repository contains my complete submission for the Backend Engineering Internship case study at Bynry.

---

## 📦 Part 1 – Product API Fix

### 🔍 Issues in Original Code
- Missing input validation for required fields
- No checks for SKU uniqueness
- Product incorrectly tied to a single warehouse
- Multiple database commits
- No error handling or rollback on failure

### ✅ Fixes Made
- Validated all fields with type checks
- Checked for duplicate SKUs before insert
- Removed warehouse link from product table
- Combined DB operations into a single transaction
- Added proper error handling and status codes

### 🧠 Assumptions
- Each product can be stored in multiple warehouses
- SKU is unique across all products
- Price is a decimal; quantity is an integer
- Warehouse must exist before adding inventory

---

## 🧱 Part 2 – Database Design

See `part2_database_schema.md` for full schema, assumptions, and design justifications.

---

## 📁 Files

- `part1_create_product_api.py` – Corrected Flask endpoint
- `part2_database_schema.md` – Full database schema and notes
