# ATM System - Requirements Analysis

## Functional Requirements (WHAT the system DOES)

1. **Card Validation**
   - Read ATM card using magnetic stripe reader
   - Accept PIN entry from keyboard
   - Validate PIN against database
   - Allow up to 3 PIN entry attempts
   - Retain card after 3 failed attempts

2. **Withdraw Cash**
   - Accept withdrawal amount only in multiples of 100
   - Validate sufficient balance available
   - Dispense cash using cash dispenser
   - Update account balance
   - Record transaction

3. **Deposit Cash**
   - Accept cash deposit in multiples of 100
   - Accept envelope through deposit slot
   - Update account balance
   - Record transaction

4. **Balance Enquiry**
   - Display current account balance on screen
   - Allow multiple balance inquiries per session

5. **Money Transfer**
   - Accept transfer amount (multiples of 100)
   - Accept destination account details
   - Validate sufficient balance
   - Deduct from source account
   - Credit to destination account
   - Record transaction

6. **Receipt Printing**
   - Print transaction details on receipt
   - Include date, time, amount, balance
   - Use printer to generate physical receipt

7. **Transaction Management**
   - Record all transactions for audit trail
   - Maintain transaction history per account
   - Support multiple transactions per session

8. **Operator Control**
   - Allow operator to start/stop machine via key switch
   - Allow operator to enter initial cash on hand


## Non-Functional Requirements (HOW the system BEHAVES)

### Performance
1. Transaction completion time: Maximum 60 seconds per transaction
2. Auto-cancel transaction if exceeded 60 seconds

### Availability & Reliability
3. 24X7 service availability
4. Machine operates continuously except during maintenance

### Concurrency & Session Management
5. Only one customer at a time
6. Card retention if machine idle for more than 2 minutes
7. Automatic session logout after 2 minutes of inactivity

### Hardware & Infrastructure
8. Magnetic stripe reader for card reading
9. Keyboard for PIN and input entry
10. Display screen for customer interaction and prompts
11. Deposit slot for cash envelopes
12. Cash dispenser for withdrawal
13. Printer for receipt generation
14. Operator panel with key switch for start/stop

### Security & Data Integrity
15. PIN validation for authentication
16. Transaction recording for audit trail
17. Data validation for all inputs
18. Secure card handling and retention mechanism

### Usability
19. Clear display prompts and messages
20. User-friendly keyboard interface


# How to Apply This to Your Management Systems

## For Each Management System (Scale Model):

### Functional Requirements Template:
- **Data Entry**: Add/Create records with validation
- **Data Retrieval**: View, search, filter records
- **Data Modification**: Update status, details
- **Data Deletion**: Remove records
- **Reports**: Generate summaries/receipts
- **Authentication**: Login/validation of users
- **Transaction Recording**: Track all operations

### Non-Functional Requirements Template:
- **Performance**: Response time limits (e.g., operations within X seconds)
- **Availability**: When system is available (e.g., 24/7, business hours)
- **Scalability**: Number of users, records handled
- **Concurrency**: Single vs multiple users
- **Security**: Authentication, authorization, encryption
- **Usability**: Interface requirements, user experience
- **Data Integrity**: Transaction consistency, audit trails
- **Hardware/UI**: Required components (forms, tables, buttons)
- **Session Management**: Timeout periods, inactivity handling
- **Error Handling**: Invalid input handling, retry mechanisms

## Example: Student Management System with Detailed Requirements

### Functional Requirements:
1. Admin login with username/password
2. Add student with validation (ID format, email format)
3. Search student by ID or name
4. Update student information
5. Delete student record
6. View detailed student profile
7. Generate enrollment report
8. Record all admin actions in activity log

### Non-Functional Requirements:
1. All operations must complete within 30 seconds
2. System available during working hours (8 AM - 6 PM)
3. Support up to 100 concurrent students in database
4. Single admin access at a time
5. Auto-logout after 15 minutes of inactivity
6. Data backup daily
7. User-friendly web interface
8. Form validation with error messages
9. Activity log maintained for audit trail
10. Password must be at least 8 characters
