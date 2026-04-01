# DFD Guide - ATM System & Management Systems

## DFD Components Overview

**Level 0 (Context Diagram)** - System as single bubble
**Level 1** - Major processes
**Level 2** - Detailed processes
**Level 3+** - Further decomposition

---

## ATM System DFD

### Level 0 (Context Diagram)
```
┌─────────────────┐
│   Customer      │ ← Enters Card, PIN, Commands, Receives Cash, Receipt
│                 │
└────────┬────────┘
         │
         ▼
    ┌─────────────┐
    │  ATM System │
    └─────────────┘
         │
         ▼ (Query/Update)
    ┌─────────────────────┐
    │   Bank Database     │
    │ (Accounts, Balances)│
    └─────────────────────┘

Also connected:
- Operator (Start/Stop, Cash replenishment)
```

### Level 1 - Main Processes
```
1. Authentication (Validate Card & PIN)
2. Transaction Processing
   - Withdrawal
   - Deposit
   - Balance Inquiry
   - Transfer
3. Receipt Generation
4. Machine Management (Operator)
```

### Level 2 - Detailed Processes (Authentication)
```
Process: Authenticate Customer
Inputs: 
  - ATM Card (from magnetic reader)
  - PIN (from keyboard)
Outputs:
  - Authenticated/Not Authenticated (to system)
  - Error Message (to display)
Data Stores:
  - Customer Database (account details, valid PINs)
  - Transaction Log (for audit)
```

---

## How to Create DFD for Your Management Systems

### Student Management System - Level 0
```
┌──────────────┐
│   Registrar  │
│   (Admin)    │
└──────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Student Management System   │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  Student Database           │
│  (Records, Details)         │
└─────────────────────────────┘
```

### Student Management System - Level 1
```
Process 1: Student Authentication
  Input: Login credentials
  Output: Access granted/denied

Process 2: Student Record Management
  Inputs: Student data
  Outputs: Confirmation messages
  
Process 3: Search & Report Generation
  Inputs: Search criteria
  Outputs: Student records, Reports
  
Process 4: Activity Logging
  Inputs: All operations
  Outputs: Activity log
```

### Student Management System - Level 2 (Example: Record Management)
```
Process 2.1: Add Student
  Inputs: Student details (name, ID, email, dept)
  Outputs: Confirmation message
  Data Store: Student Database
  
Process 2.2: Update Student
  Inputs: Student ID, Updated data
  Outputs: Update confirmation
  
Process 2.3: Delete Student
  Inputs: Student ID
  Outputs: Deletion confirmation
```

---

## Template for DFD Analysis

### For Each Management System:

**External Entities:**
- Users/Admin
- System Operators
- End Users (Customers/Students/Patients, etc.)

**Processes (Main):**
1. Authentication
2. Add/Create (Data Entry)
3. Read/View/Search (Data Retrieval)
4. Update/Modify (Data Modification)
5. Delete (Data Removal)
6. Reports/Analytics
7. System Administration

**Data Stores:**
- Main Database (All records)
- Transaction/Activity Log
- User/Admin Database
- Configuration Data

**Data Flows:**
- From External Entities to Processes
- Between Processes
- From Processes to Data Stores
- From Data Stores back to Processes

---

## Example: Restaurant Management System - Level 1 DFD

```
External Entities:
├─ Chef/Manager (Admin)
├─ Staff (Order handlers)
└─ Customer (Places order)

Processes:
1. Authentication (Chef/Staff login)
2. Menu Management (Add/Update items)
3. Order Processing (Place, Update, Complete)
4. Billing & Reports
5. Inventory Management

Data Stores:
├─ Menu Database
├─ Order Database
├─ Customer Database
├─ Inventory Database
└─ Transaction Log
```

---

## Key Points for Exam

1. **Identify all entities** that interact with your system
2. **List main processes** without too much detail (Level 1)
3. **Show data flows** clearly between entities and processes
4. **Include data stores** with appropriate database names
5. **Use standard DFD symbols**:
   - Rectangle: External Entity
   - Circle/Bubble: Process
   - Parallel lines: Data Store
   - Arrows: Data Flows

6. **For Level 2 DFD**: Expand one process into sub-processes
7. **Clarity over complexity** - Don't overcrowd the diagram
8. **Label all flows** with names of data being transferred

---

## Requirements to DFD Mapping

**Functional Requirements** → Become **Processes** in DFD
Example: "Withdraw cash" → Process "Process Withdrawal"

**Non-Functional Requirements** → Constraints on **Data Flows & Processes**
Example: "60-second timeout" → Added as note near process

**Data Requirements** → **Data Stores** in DFD
Example: "Transaction recording" → Data store "Transaction Log"

**Hardware/UI Requirements** → Shown as part of **External Entities**
Example: "Keyboard/Display" → ATM hardware entity
