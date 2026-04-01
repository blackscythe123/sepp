import streamlit as st

st.title("Restaurant Management System")

if 'menu_items' not in st.session_state:
    st.session_state.menu_items = []
if 'orders' not in st.session_state:
    st.session_state.orders = []

tab1, tab2, tab3 = st.tabs(["Menu", "Place Order", "Orders"])

with tab1:
    st.subheader("Add Menu Item")
    item_id = st.text_input("Item ID", key="iid")
    item_name = st.text_input("Dish Name", key="idish")
    item_category = st.text_input("Category", key="icat")
    item_price = st.number_input("Price", min_value=0.0, key="iprice")
    
    if st.button("Add Item"):
        if item_id and item_name:
            st.session_state.menu_items.append({
                'id': item_id,
                'name': item_name,
                'category': item_category,
                'price': item_price
            })
            st.success("Menu item added!")
        else:
            st.error("Fill required fields")
    
    st.subheader("Current Menu")
    if st.session_state.menu_items:
        for idx, item in enumerate(st.session_state.menu_items):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{item['name']}** ({item['category']}) - Rs. {item['price']}")
                st.write(f"Item ID: {item['id']}")
            with col2:
                if st.button("Delete", key=f"del_item_{idx}"):
                    st.session_state.menu_items.pop(idx)
                    st.rerun()
    else:
        st.info("No menu items added")

with tab2:
    st.subheader("Place Order")
    if st.session_state.menu_items:
        order_id = st.text_input("Order ID", key="oid")
        item_id = st.selectbox("Select Item", [i['id'] for i in st.session_state.menu_items])
        quantity = st.number_input("Quantity", min_value=1, key="oqty")
        
        if st.button("Place Order"):
            item = [i for i in st.session_state.menu_items if i['id'] == item_id][0]
            order = {
                'orderId': order_id,
                'itemId': item_id,
                'itemName': item['name'],
                'quantity': quantity,
                'totalAmount': item['price'] * quantity,
                'status': 'Pending'
            }
            st.session_state.orders.append(order)
            st.success("Order placed successfully!")
            st.rerun()
    else:
        st.warning("Add menu items first")

with tab3:
    st.subheader("Orders")
    if st.session_state.orders:
        for idx, order in enumerate(st.session_state.orders):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**Order ID:** {order['orderId']} | **Item:** {order['itemName']} | **Qty:** {order['quantity']}")
                st.write(f"**Total:** Rs. {order['totalAmount']} | **Status:** {order['status']}")
            with col2:
                if st.button("Complete", key=f"comp_order_{idx}"):
                    order['status'] = 'Completed'
                    st.rerun()
    else:
        st.info("No orders placed yet")
