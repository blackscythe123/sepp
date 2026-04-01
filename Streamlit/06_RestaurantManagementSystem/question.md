# RESTAURANT MANAGEMENT SYSTEM - Exam Question

## Scenario
A restaurant needs a system to manage menu items and process customer orders. Staff should be able to add menu items, place orders, track order status, and generate bills.

## Requirements

### Functional Requirements
- Add menu items with ID, Name, Category, Price
- Display complete menu with categories
- Place orders with Order ID, Item selection, Quantity
- Track order status (Pending/Preparing/Ready/Served)
- Calculate order total amount
- Generate bill for completed orders
- Delete cancelled orders
- Search orders by ID or status

### Non-Functional Requirements
- Operations complete within 30 seconds
- Support 500+ daily orders
- Real-time order tracking
- Prevent duplicate orders
- Clear status updates

## Implementation Guidelines
1. Build using Python with Streamlit
2. Sections: Add Menu, View Menu, Place Order, Track Order, Generate Bill
3. Store menu and order data using session state
4. Implement order status workflow
5. Calculate totals and generate bills
6. Track order history

## Deliverables
- Menu management system
- Order processing application
- Order tracking and status updates
- Bill generation system
- Order history and search
- Category-wise menu display
- Daily order summary

## Marks Distribution (Total: 20 marks)
- Menu Management: 3 marks
- Order Placement: 4 marks
- Order Status Tracking: 4 marks
- Bill Generation: 3 marks
- Amount Calculations: 3 marks
- Validation: 3 marks

---
**Time Limit:** 60 minutes
**Language:** Python (Streamlit)
