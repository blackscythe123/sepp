# INVENTORY MANAGEMENT SYSTEM - Exam Question

## Scenario
A warehouse needs an inventory management system to track products, stock levels, and generate low-stock alerts. The manager should be able to add products, update stock, and monitor inventory.

## Requirements

### Functional Requirements
- Add product with Product ID, Name, Quantity, Price
- View all products with calculated total value
- Update stock quantity (add/subtract)
- Delete product from inventory
- Search product by ID or Name
- Generate low stock alert (quantity < 20)
- Calculate total inventory value
- Track stock movement history

### Non-Functional Requirements
- Operations complete within 30 seconds
- Support 10,000+ products
- Real-time inventory updates
- Clear warning for low stock items
- Prevent negative stock quantities

## Implementation Guidelines
1. Build using Python with Streamlit
2. Sections: Add Product, View Inventory, Update Stock, Low Stock Alert
3. Store product data using session state
4. Calculate and display product value (Qty × Price)
5. Implement validation for quantities and prices
6. Show real-time inventory statistics

## Deliverables
- Complete inventory management application
- Product database with stock levels
- Stock update functionality
- Low stock alert system
- Inventory value calculation
- Search and filter products
- Stock movement tracking

## Marks Distribution (Total: 20 marks)
- Product Management: 4 marks
- Stock Update: 4 marks
- Calculations: 3 marks
- Low Stock Alert: 3 marks
- Search & Analytics: 3 marks
- Validation: 3 marks

---
**Time Limit:** 60 minutes
**Language:** Python (Streamlit)
