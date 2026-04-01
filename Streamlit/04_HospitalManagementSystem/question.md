# HOSPITAL MANAGEMENT SYSTEM - Exam Question

## Scenario
A hospital needs a system to manage patient records and track patient status. The doctor/administrator should be able to register patients, update their status, and maintain medical records.

## Requirements

### Functional Requirements
- Register patient with ID, Name, Age, Disease, Doctor assigned
- Display all patient records
- Update patient status (Admitted/Under Treatment/Discharged/Critical)
- Search patient by ID or Name
- Delete patient record
- Track admission and discharge dates
- Report critical patients
- Display patient-doctor association

### Non-Functional Requirements
- Operations within 30 seconds
- Support 50,000+ patient records
- Priority display for critical patients
- Clear status indicators
- Confirmation before status changes
- 24/7 system availability

## Implementation Guidelines
1. Build using Python with Streamlit
2. Sections: Register Patient, View Records, Search, Update Status, Critical Alert
3. Store patient data using session state
4. Implement status update workflow
5. Show date and time tracking
6. Highlight critical patients

## Deliverables
- Patient registration and management system
- Patient record database
- Status tracking and updates
- Search by patient ID or name
- Critical patient alert system
- Doctor-patient mapping
- Admission-discharge tracking

## Marks Distribution (Total: 20 marks)
- Patient Registration: 3 marks
- View & Search: 3 marks
- Status Update: 4 marks
- Critical Alert: 3 marks
- Data Tracking: 3 marks
- Validation: 4 marks

---
**Time Limit:** 60 minutes
**Language:** Python (Streamlit)
