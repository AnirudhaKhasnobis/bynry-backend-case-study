# Bynry Backend Internship – Case Study Submission

This repository contains my complete submission for the Backend Engineering Internship case study at Bynry Inc.

---

## ✅ Part 1 – Product API Fix

### 🔍 Issues Found
- Missing input validation and type checks
- No check for duplicate SKUs
- Product incorrectly tied to a single warehouse
- Multiple DB commits instead of one transaction
- No error handling or rollback

### 💡 Fixes Made
- Added input validation and type checking
- Checked for existing SKUs before insertion
- Stored inventory separately from the product
- Combined operations into a single DB transaction
- Added proper error handling and status codes

---

## ✅ Part 2 – Database Design

See `part2_database_schema.md` for:
- Full schema (tables + keys)
- Assumptions and business questions
- Design reasoning

---

## ✅ Part 3 – Low Stock Alerts API

See `part3_low_stock_api.py` for:
- Complete Flask route to generate low-stock alerts
- Example JSON output
- Comments and assumptions included

---

## 📁 Files

- `part1_create_product_api.py` – Fixed product creation endpoint
- `part2_database_schema.md` – Database schema and explanations
- `part3_low_stock_api.py` – Low-stock alert implementation
