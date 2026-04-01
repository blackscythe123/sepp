import streamlit as st

st.title("Inventory Management System")

if 'products' not in st.session_state:
    st.session_state.products = []

tab1, tab2, tab3 = st.tabs(["Add Product", "Inventory", "Update Stock"])

with tab1:
    st.subheader("Add New Product")
    product_id = st.text_input("Product ID", key="pid")
    product_name = st.text_input("Product Name", key="pname")
    product_qty = st.number_input("Quantity", min_value=0, key="pqty")
    product_price = st.number_input("Price", min_value=0.0, key="pprice")
    
    if st.button("Add Product"):
        if product_id and product_name:
            st.session_state.products.append({
                'id': product_id,
                'name': product_name,
                'quantity': product_qty,
                'price': product_price
            })
            st.success("Product added successfully!")
        else:
            st.error("Please fill all fields")

with tab2:
    st.subheader("Product Inventory")
    if st.session_state.products:
        for idx, product in enumerate(st.session_state.products):
            total_value = product['quantity'] * product['price']
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{product['name']}** (ID: {product['id']})")
                st.write(f"Quantity: {product['quantity']} | Price: {product['price']} | Total Value: {total_value:.2f}")
            with col2:
                if st.button("Delete", key=f"del_prod_{idx}"):
                    st.session_state.products.pop(idx)
                    st.rerun()
    else:
        st.info("No products in inventory")
    
    st.subheader("Low Stock Alert (Less than 20)")
    low_stock = [p for p in st.session_state.products if p['quantity'] < 20]
    if low_stock:
        st.warning("Low Stock Items:")
        for item in low_stock:
            st.write(f"- {item['name']} (Qty: {item['quantity']})")
    else:
        st.success("All items have sufficient stock")

with tab3:
    st.subheader("Update Stock")
    if st.session_state.products:
        product_id = st.selectbox("Select Product", [p['id'] for p in st.session_state.products])
        qty_change = st.number_input("Quantity to add/subtract", value=0, key="qtychange")
        
        if st.button("Update Stock"):
            for product in st.session_state.products:
                if product['id'] == product_id:
                    product['quantity'] += qty_change
                    st.success("Stock updated!")
                    st.rerun()
    else:
        st.info("No products to update")
