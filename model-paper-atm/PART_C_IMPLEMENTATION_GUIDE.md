# PART C - Implementation Guide (Simple HTML/Streamlit)

## What is Expected in Part C?

**Question:** Build a basic web application to demonstrate the functionality described in Parts A & B.

**Important:** You are NOT expected to build a full-stack system. Keep it simple, focused, and working.

---

## Implementation Checklist for HTML Version

### ✓ Must Have Features:
- [ ] Simple HTML forms (no CSS styling)
- [ ] Vanilla JavaScript for logic
- [ ] CRUD operations (Create, Read, Update, Delete)
- [ ] Basic data validation
- [ ] Display results in tables/lists
- [ ] Working search/filter functionality

### ✓ Data Storage:
- [ ] Use JavaScript arrays or localStorage
- [ ] Store data in browser memory (NOT database)
- [ ] No backend server needed

### ✓ User Interface:
- [ ] Clear headings for each section
- [ ] Input fields with labels
- [ ] Buttons for actions
- [ ] Error messages for invalid input
- [ ] Success messages for operations
- [ ] Simple, readable layout


---

## Implementation Checklist for Streamlit Version

### ✓ Must Have Features:
- [ ] Multiple tabs or sections for operations
- [ ] Forms using Streamlit widgets (st.text_input, st.button, etc.)
- [ ] Session state management (st.session_state)
- [ ] CRUD operations using list/dictionary storage
- [ ] Display results using st.table or st.write
- [ ] Search/filter with conditional logic

### ✓ Structure:
- [ ] Clear title and headings
- [ ] Organized tabs/sections
- [ ] Input validation with error handling
- [ ] Success/warning messages
- [ ] Readable output formatting


---

## HTML Template - Student Management (Part C Example)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>
</head>
<body>
    <h1>Student Management System</h1>
    
    <!-- Section 1: Add Student -->
    <h2>Add Student</h2>
    <form id="addForm">
        <input type="text" id="studentId" placeholder="Student ID" required>
        <input type="text" id="studentName" placeholder="Name" required>
        <input type="email" id="studentEmail" placeholder="Email" required>
        <input type="text" id="studentDept" placeholder="Department" required>
        <button type="submit">Add</button>
    </form>
    
    <!-- Section 2: View Students -->
    <h2>Student List</h2>
    <table id="studentTable" border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Department</th>
            <th>Action</th>
        </tr>
    </table>
    
    <!-- Section 3: Search Student -->
    <h2>Search Student</h2>
    <input type="text" id="searchId" placeholder="Enter Student ID">
    <button onclick="searchStudent()">Search</button>
    <div id="searchResult"></div>
    
    <!-- Section 4: Filter by Department -->
    <h2>Filter by Department</h2>
    <input type="text" id="filterDept" placeholder="Enter Department">
    <button onclick="filterDept()">Filter</button>
    <div id="filterResult"></div>
    
    <script>
        let students = [];
        
        // Add Student
        document.getElementById('addForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            let student = {
                id: document.getElementById('studentId').value,
                name: document.getElementById('studentName').value,
                email: document.getElementById('studentEmail').value,
                dept: document.getElementById('studentDept').value
            };
            
            // Validation
            if (!student.id || !student.name || !student.email || !student.dept) {
                alert('Please fill all fields');
                return;
            }
            
            // Duplicate check
            if (students.find(s => s.id === student.id)) {
                alert('Student ID already exists');
                return;
            }
            
            students.push(student);
            alert('Student added successfully');
            displayStudents();
            this.reset();
        });
        
        // Display Students
        function displayStudents() {
            let html = '<tr><th>ID</th><th>Name</th><th>Email</th><th>Department</th><th>Action</th></tr>';
            
            students.forEach((student, index) => {
                html += `<tr>
                    <td>${student.id}</td>
                    <td>${student.name}</td>
                    <td>${student.email}</td>
                    <td>${student.dept}</td>
                    <td><button onclick="deleteStudent(${index})">Delete</button></td>
                </tr>`;
            });
            
            document.getElementById('studentTable').innerHTML = html;
        }
        
        // Delete Student
        function deleteStudent(index) {
            if (confirm('Are you sure?')) {
                students.splice(index, 1);
                alert('Student deleted');
                displayStudents();
            }
        }
        
        // Search Student
        function searchStudent() {
            let id = document.getElementById('searchId').value;
            let result = students.find(s => s.id === id);
            
            if (result) {
                document.getElementById('searchResult').innerHTML = `
                    <h3>Found Student:</h3>
                    <p>ID: ${result.id}</p>
                    <p>Name: ${result.name}</p>
                    <p>Email: ${result.email}</p>
                    <p>Department: ${result.dept}</p>
                `;
            } else {
                document.getElementById('searchResult').innerHTML = '<p>Not found</p>';
            }
        }
        
        // Filter by Department
        function filterDept() {
            let dept = document.getElementById('filterDept').value;
            let filtered = students.filter(s => s.dept.toLowerCase() === dept.toLowerCase());
            
            if (filtered.length > 0) {
                let html = `<h3>Students in ${dept}:</h3><table border="1"><tr><th>ID</th><th>Name</th><th>Email</th></tr>`;
                
                filtered.forEach(student => {
                    html += `<tr>
                        <td>${student.id}</td>
                        <td>${student.name}</td>
                        <td>${student.email}</td>
                    </tr>`;
                });
                
                html += '</table>';
                document.getElementById('filterResult').innerHTML = html;
            } else {
                document.getElementById('filterResult').innerHTML = '<p>No students in this department</p>';
            }
        }
    </script>
</body>
</html>
```

---

## Streamlit Template - Student Management (Part C Example)

```python
import streamlit as st

st.set_page_config(page_title="Student Management System", layout="wide")

st.title("Student Management System")

# Initialize session state
if 'students' not in st.session_state:
    st.session_state.students = []

# Create tabs for different operations
tab1, tab2, tab3, tab4 = st.tabs(["Add Student", "View All", "Search", "Analytics"])

# TAB 1: Add Student
with tab1:
    st.subheader("Add New Student")
    
    col1, col2 = st.columns(2)
    
    with col1:
        student_id = st.text_input("Student ID", key="sid")
        student_name = st.text_input("Student Name", key="sname")
    
    with col2:
        student_email = st.text_input("Email", key="semail")
        student_dept = st.text_input("Department", key="sdept")
    
    if st.button("Add Student", key="add_btn"):
        # Validation
        if not student_id or not student_name or not student_email or not student_dept:
            st.error("Please fill all fields")
        elif any(s['id'] == student_id for s in st.session_state.students):
            st.error("Student ID already exists")
        else:
            st.session_state.students.append({
                'id': student_id,
                'name': student_name,
                'email': student_email,
                'dept': student_dept
            })
            st.success("Student added successfully!")
            st.rerun()

# TAB 2: View All Students
with tab2:
    st.subheader("All Students")
    
    if st.session_state.students:
        for idx, student in enumerate(st.session_state.students):
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.write(f"**ID:** {student['id']} | **Name:** {student['name']}")
                st.write(f"**Email:** {student['email']} | **Department:** {student['dept']}")
            
            with col2:
                if st.button("Delete", key=f"del_{idx}"):
                    st.session_state.students.pop(idx)
                    st.rerun()
            
            st.divider()
    else:
        st.info("No students added yet")

# TAB 3: Search Student
with tab3:
    st.subheader("Search Student")
    
    search_id = st.text_input("Enter Student ID", key="search_id")
    
    if st.button("Search", key="search_btn"):
        result = [s for s in st.session_state.students if s['id'] == search_id]
        
        if result:
            student = result[0]
            st.success("Student Found!")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**ID:** {student['id']}")
                st.write(f"**Name:** {student['name']}")
            
            with col2:
                st.write(f"**Email:** {student['email']}")
                st.write(f"**Department:** {student['dept']}")
        else:
            st.warning("Student not found")

# TAB 4: Analytics
with tab4:
    st.subheader("Department Analytics")
    
    if st.session_state.students:
        # Count by department
        dept_count = {}
        for student in st.session_state.students:
            dept = student['dept']
            dept_count[dept] = dept_count.get(dept, 0) + 1
        
        st.write("**Students by Department:**")
        for dept, count in dept_count.items():
            st.write(f"- {dept}: {count} students")
        
        st.write(f"\n**Total Students:** {len(st.session_state.students)}")
    else:
        st.info("No data to display")
```

---

## How to Run

### HTML:
Simply open the `.html` file in a web browser.

### Streamlit:
```bash
streamlit run app.py
```

---

## Testing Your Implementation

Before submitting, test these scenarios:

1. **Add Operation:**
   - ✓ Add valid record
   - ✓ Try adding with empty fields (should show error)
   - ✓ Try adding duplicate ID (should show error)

2. **View Operation:**
   - ✓ View all records
   - ✓ Records display in table/list format

3. **Search Operation:**
   - ✓ Search for existing record
   - ✓ Search for non-existing record (should show not found)

4. **Delete Operation:**
   - ✓ Delete existing record
   - ✓ Record is removed from list

5. **Filter/Analytics:**
   - ✓ Filter by department shows correct results
   - ✓ Count by department is accurate

---

## Common Mistakes to AVOID:

❌ Don't build complex database systems
❌ Don't focus on fancy styling/CSS
❌ Don't make it too complicated
❌ Don't forget data validation
❌ Don't make the UI confusing
✓ Keep it SIMPLE and FUNCTIONAL

---

## Marks Distribution (Approx for Part C - 20 marks):

- **Functionality (8 marks):** CRUD works, validation present
- **Code Quality (5 marks):** Clean, readable, properly commented
- **UI/UX (4 marks):** Clear, easy to use, messages visible
- **Error Handling (3 marks):** Handles invalid input gracefully

Remember: It's better to have a simple, working system than a complex broken one!
