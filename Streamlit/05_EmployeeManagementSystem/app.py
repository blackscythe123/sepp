import streamlit as st

st.title("Employee Management System")

if 'employees' not in st.session_state:
    st.session_state.employees = []

tab1, tab2, tab3 = st.tabs(["Add Employee", "Directory", "Analytics"])

with tab1:
    st.subheader("Add Employee")
    emp_id = st.text_input("Employee ID", key="eid")
    emp_name = st.text_input("Employee Name", key="ename")
    emp_dept = st.text_input("Department", key="edept")
    emp_position = st.text_input("Position", key="epos")
    emp_salary = st.number_input("Salary", min_value=0.0, key="esal")
    
    if st.button("Add Employee"):
        if emp_id and emp_name:
            st.session_state.employees.append({
                'id': emp_id,
                'name': emp_name,
                'dept': emp_dept,
                'position': emp_position,
                'salary': emp_salary
            })
            st.success("Employee added successfully!")
        else:
            st.error("Please fill required fields")

with tab2:
    st.subheader("Employee Directory")
    if st.session_state.employees:
        for idx, emp in enumerate(st.session_state.employees):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{emp['name']}** (ID: {emp['id']})")
                st.write(f"Department: {emp['dept']} | Position: {emp['position']} | Salary: {emp['salary']}")
            with col2:
                if st.button("Delete", key=f"del_emp_{idx}"):
                    st.session_state.employees.pop(idx)
                    st.rerun()
    else:
        st.info("No employees in directory")
    
    st.subheader("Filter by Department")
    dept = st.text_input("Enter Department Name")
    if st.button("Filter"):
        filtered = [e for e in st.session_state.employees if e['dept'].lower() == dept.lower()]
        if filtered:
            st.success(f"Employees in {dept}:")
            for emp in filtered:
                st.write(f"- {emp['name']} ({emp['position']}) - Salary: {emp['salary']}")
        else:
            st.warning("No employees in this department")

with tab3:
    st.subheader("Department Analytics")
    if st.session_state.employees:
        dept_map = {}
        for emp in st.session_state.employees:
            dept_map[emp['dept']] = dept_map.get(emp['dept'], 0) + 1
        
        st.write("**Employee Count by Department:**")
        for dept, count in dept_map.items():
            st.write(f"- {dept}: {count} employees")
        
        total_salary = sum(e['salary'] for e in st.session_state.employees)
        st.write(f"**Total Salary Cost:** {total_salary}")
    else:
        st.info("No employees to analyze")
