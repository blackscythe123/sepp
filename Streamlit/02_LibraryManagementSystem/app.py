import streamlit as st

st.title("Library Management System")

if 'books' not in st.session_state:
    st.session_state.books = []

tab1, tab2, tab3 = st.tabs(["Add Book", "Book List", "Issue/Return"])

with tab1:
    st.subheader("Add New Book")
    book_id = st.text_input("Book ID", key="bid")
    book_title = st.text_input("Book Title", key="btitle")
    book_author = st.text_input("Author", key="bauthor")
    book_isbn = st.text_input("ISBN", key="bisbn")
    
    if st.button("Add Book"):
        if book_id and book_title and book_author and book_isbn:
            st.session_state.books.append({
                'id': book_id,
                'title': book_title,
                'author': book_author,
                'isbn': book_isbn,
                'status': 'Available'
            })
            st.success("Book added successfully!")
        else:
            st.error("Please fill all fields")

with tab2:
    st.subheader("Book Inventory")
    if st.session_state.books:
        for idx, book in enumerate(st.session_state.books):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{book['title']}** by {book['author']}")
                st.write(f"ID: {book['id']} | ISBN: {book['isbn']} | Status: {book['status']}")
            with col2:
                if st.button("Delete", key=f"del_book_{idx}"):
                    st.session_state.books.pop(idx)
                    st.rerun()
    else:
        st.info("No books in inventory")

with tab3:
    st.subheader("Issue/Return Book")
    action = st.radio("Select Action", ["Issue Book", "Return Book"])
    
    if action == "Issue Book":
        book_id = st.selectbox("Select Book", [b['id'] for b in st.session_state.books if b['status'] == 'Available'])
        member_id = st.text_input("Member ID")
        
        if st.button("Issue Book"):
            for book in st.session_state.books:
                if book['id'] == book_id:
                    book['status'] = f"Issued to {member_id}"
                    st.success("Book issued successfully!")
                    st.rerun()
    
    else:
        book_id = st.selectbox("Select Book to Return", [b['id'] for b in st.session_state.books])
        
        if st.button("Return Book"):
            for book in st.session_state.books:
                if book['id'] == book_id:
                    book['status'] = "Available"
                    st.success("Book returned successfully!")
                    st.rerun()
