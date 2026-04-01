# STUDENT MANAGEMENT SYSTEM - Exam Question

## Scenario
A college needs a software system to manage student records. The registrar should be able to add, view, search, and delete student information. The system must maintain an audit log of all operations.

## Requirements

### Functional Requirements
- Add new student with ID, Name, Email, and Department
- View all students in a list format
- Search student by ID or Name
- Delete student record with confirmation
- Update student department
- Prevent duplicate Student IDs
- Validate email format
- Log all operations with timestamp

### Non-Functional Requirements
- All operations must complete within 30 seconds
- Support up to 5000 student records
- Auto-logout after 15 minutes inactivity
- Clear error messages for invalid operations
- Display confirmation dialogs for delete operations

## Implementation Guidelines
1. Build using Python with Streamlit
2. Implement CRUD operations
3. Use session state for data storage
4. Include input validation
5. Display results in dataframes/tables
6. Show success and error messages
7. Create an activity log section

## Deliverables
- Fully functional Streamlit application with all CRUD operations
- Input validation with error handling
- Activity log with timestamps
- Search and filter capabilities
- Statistics dashboard

## Marks Distribution (Total: 20 marks)
- User Interface: 4 marks
- Add/Create: 3 marks
- View/Search: 3 marks
- Update/Delete: 3 marks
- Validation: 4 marks
- Activity Log: 2 marks
- Code Quality: 1 mark

---
**Time Limit:** 60 minutes
**Language:** Python (Streamlit)
