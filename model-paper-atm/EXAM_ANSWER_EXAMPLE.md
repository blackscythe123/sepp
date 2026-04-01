# Complete Exam Answer Example - Student Management System

This document shows how to answer Part A & B of the exam with proper Requirements Analysis and DFD/Activity Diagram design.

---

## PART A - Requirements Analysis (15 marks)

### Scenario:
"A software system is to be built to manage student records in a college. The system should allow the registrar to add, view, search, and manage student information. Each operation must complete within 30 seconds. The system should prevent unauthorized access and maintain an activity log of all operations."

---

### FUNCTIONAL REQUIREMENTS (What the system DOES):

1. **Student Record Management**
   - Add new student with details (ID, Name, Email, Department, Contact)
   - Update existing student information
   - Delete student record
   - View individual student details

2. **Search & Retrieval**
   - Search student by ID
   - Search student by name
   - Filter students by department
   - View list of all students

3. **Authentication & Authorization**
   - Login registrar with username and password
   - Validate access credentials
   - Prevent unauthorized access

4. **Activity Logging**
   - Record all add operations
   - Record all update operations
   - Record all delete operations
   - Record search operations
   - Maintain timestamp for each operation

5. **Report Generation**
   - Generate department-wise student count
   - Generate activity report
   - Export student list


### NON-FUNCTIONAL REQUIREMENTS (HOW the system BEHAVES):

**Performance:**
1. All operations must complete within 30 seconds
2. Search results must display within 5 seconds
3. Student list must load within 10 seconds

**Availability:**
4. System available during office hours (8 AM - 6 PM)
5. System should be accessible to authorized registrars only

**Scalability:**
6. Support up to 5000 student records
7. Support concurrent access by max 2 registrars

**Security:**
8. Authentication required before any operation
9. Password must be minimum 8 characters with alphanumeric
10. All data must be validated before storage

**Concurrency & Session Management:**
11. Auto-logout after 15 minutes of inactivity
12. One registrar operation at a time
13. Lock mechanism for simultaneous updates

**Usability:**
14. User-friendly interface with clear prompts
15. Error messages for invalid operations
16. Confirmation dialogs for delete operations

**Data Integrity:**
17. No duplicate student IDs allowed
18. Email format validation
19. Transaction log maintained for audit
20. Backup daily at 6 PM

---

## PART B - Design (DFD & Activity Diagram) (20 marks)

### Level 0 DFD (Context Diagram)

```
             ┌──────────────────┐
             │   Registrar      │
             │   (Admin User)   │
             └──────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
    (Student   (Query/Update) (Reports)
     Details)

┌──────────────────────────────────┐
│   Student Management System      │
│                                  │
│  - Authentication                │
│  - Student Records Management    │
│  - Search & Filter               │
│  - Report Generation             │
│  - Activity Logging              │
└──────────────────────────────────┘
        ▲             ▲
        │             │
    (Data)        (Data)
        │             │
        ▼             ▼
┌──────────────────────────────────┐
│    Data (Databases)              │
│                                  │
│  - Student Database              │
│  - User/Registrar Database       │
│  - Activity Log Database         │
└──────────────────────────────────┘
```

---

### Level 1 DFD (Top Level Processes)

```
                  ┌─────────────────┐
                  │   Registrar     │
                  └────────┬────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
    ┌────────┐        ┌────────┐        ┌────────┐
    │Process │        │Process │        │Process │
    │  1.0   │        │  2.0   │        │  3.0   │
    │ Authen-│        │Student │        │ Report │
    │ ticate │        │Records │        │Generat-│
    │        │        │Manage- │        │ ion    │
    └────────┘        │ment    │        └────────┘
        │             └────────┘             │
        │                  │                 │
        └──────────────────┼─────────────────┘
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
            ┌──────────────┐    ┌──────────────┐
            │ Data Store   │    │ Data Store   │
            │  D1: User DB │    │  D2: Student │
            └──────────────┘    │     DB       │
                                └──────────────┘
                                     │
                                     ▼
                                ┌──────────────┐
                                │ Data Store   │
                                │  D3: Activity│
                                │  Log DB      │
                                └──────────────┘
```

---

### Level 2 DFD (Process 2.0 - Student Records Management - DETAILED)

```
                    ┌─────────────────┐
                    │   Registrar     │
                    │   (Admin)       │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
   ┌─────────┐          ┌─────────┐         ┌─────────┐
   │Process  │          │Process  │         │Process  │
   │  2.1    │          │  2.2    │         │  2.3    │
   │  Add    │          │ Update  │         │ Delete  │
   │Student  │          │ Student │         │ Student │
   │  Data   │          │  Data   │         │  Data   │
   └────┬────┘          └────┬────┘         └────┬────┘
        │                    │                   │
        │         ┌──────────┴───────────┐       │
        │         │                      │       │
        └─────────┼──────────────────────┼───────┘
                  │                      │
                  ▼                      ▼
            ┌──────────────┐        ┌──────────────┐
            │ Data Store   │        │ Data Store   │
            │  D2: Student │        │  D3: Activity│
            │     DB       │        │    Log DB    │
            └──────────────┘        └──────────────┘

            Validation: Student ID unique, Email format valid
```

---

### Activity Diagram - Add Student Flow

```
Start
  │
  ▼
┌─────────────────┐
│ Registrar Login │
└────────┬────────┘
         │
         ▼
     ┌────────┐     No
     │Valid?  ├─────────┐
     └───┬────┘         │
     Yes │              ▼
         │         ┌──────────┐
         │         │Retry/Exit│
         │         └──────────┘
         ▼
┌─────────────────────┐
│Click Add Student    │
│Button              │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│Display Form with    │
│Input Fields:        │
│-Student ID          │
│-Name               │
│-Email              │
│-Department         │
│-Contact            │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│Registrar Enters     │
│Student Details      │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│Validate Input:      │
│-ID format          │
│-Email format       │
│-No duplicates      │
└────┬────────────────┘
     │
     ├─ Invalid ──┐
     │            ▼
     │       ┌──────────────┐
     │       │Show Error    │
     │       │Message       │
     │       └──────────────┘
     │            │
     │            └─ Retry
     │
     ├─ Valid ──┐
              ▼
         ┌─────────────────────┐
         │Store in Student DB  │
         └────────┬────────────┘
                  │
                  ▼
         ┌─────────────────────┐
         │Log Operation in     │
         │Activity Log DB      │
         └────────┬────────────┘
                  │
                  ▼
         ┌─────────────────────┐
         │Display Success      │
         │Message              │
         └────────┬────────────┘
                  │
                  ▼
         ┌─────────────────────┐
         │Prompt Next Action   │
         └─────────┬───────────┘
                   │
                   ▼
                 End
```

---

### Activity Diagram - Search Student Flow

```
Start
  │
  ▼
┌─────────────────┐
│Registrar Login  │
└────────┬────────┘
         │
         ▼
    ┌────────┐     No
    │Valid?  ├─────────┐
    └───┬────┘         │
    Yes │              ▼
        │         ┌──────────┐
        │         │Exit      │
        │         └──────────┘
        ▼
┌─────────────────────┐
│Display Search Form  │
│Search by:          │
│1.Student ID        │
│2.Name              │
│3.Department        │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│Registrar enters     │
│search criteria      │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│Query Student DB     │
│with given criteria  │
└────────┬────────────┘
         │
         ├─ Found ──┐
         │          ▼
         │     ┌──────────────┐
         │     │Display Search│
         │     │Results       │
         │     └──────────────┘
         │
         ├─ Not Found ──┐
                        ▼
                   ┌──────────────┐
                   │Display "No   │
                   │Results Found"│
                   └──────────────┘
         │
         ▼
┌─────────────────────┐
│Log Search Operation │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│Prompt Next Action   │
└────────┬────────────┘
         │
         ▼
        End
```

---

## Key Points for Answer:

✓ Separate Functional and Non-Functional clearly
✓ List at least 15-20 requirements total
✓ Use proper DFD symbols and notation
✓ Show data flows clearly
✓ Include all data stores
✓ Activity diagram shows user interaction flow
✓ Add decision points (validation, conditions)
✓ Include error handling paths
✓ Proper labeling of all processes and data stores
✓ Connect everything logically

---

## How to Adapt This for Other Systems:

Simply replace:
- "Student" with the main entity (Book, Patient, Order, etc.)
- "Registrar" with appropriate user role
- Add/Update/Delete/Search with operations specific to your system
- Database name from "Student DB" to appropriate name
- Fields in forms match your system's data model
