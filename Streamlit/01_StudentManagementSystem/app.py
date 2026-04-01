import streamlit as st

st.title("Student Management System")

if 'students' not in st.session_state:
    st.session_state.students = []

col1, col2 = st.columns(2)

with col1:
    st.subheader("Add Student")
    student_id = st.text_input("Student ID", key="sid")
    student_name = st.text_input("Student Name", key="sname")
    student_email = st.text_input("Email", key="semail")
    student_dept = st.text_input("Department", key="sdept")
    
    if st.button("Add Student"):
        if student_id and student_name and student_email and student_dept:
            st.session_state.students.append({
                'id': student_id,
                'name': student_name,
                'email': student_email,
                'dept': student_dept
            })
            st.success("Student added successfully!")
        else:
            st.error("Please fill all fields")

with col2:
    st.subheader("Search Student")
    search_id = st.text_input("Enter Student ID to search")
    if st.button("Search"):
        result = [s for s in st.session_state.students if s['id'] == search_id]
        if result:
            st.success("Student Found!")
            student = result[0]
            st.write(f"**ID:** {student['id']}")
            st.write(f"**Name:** {student['name']}")
            st.write(f"**Email:** {student['email']}")
            st.write(f"**Department:** {student['dept']}")
        else:
            st.warning("Student not found")

st.subheader("Student List")
if st.session_state.students:
    for idx, student in enumerate(st.session_state.students):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.write(f"ID: {student['id']} | Name: {student['name']} | Email: {student['email']} | Dept: {student['dept']}")
        with col2:
            if st.button("Delete", key=f"del_{idx}"):
                st.session_state.students.pop(idx)
                st.rerun()
else:
    st.info("No students added yet")
