# LIBRARY MANAGEMENT SYSTEM - Exam Question

## Scenario
A library needs a system to manage books and track book issues/returns. The librarian should be able to add books, issue books to members, return books, and check availability.

## Requirements

### Functional Requirements
- Add new book with Book ID, Title, Author, ISBN
- Display all books with status (Available/Issued)
- Issue book to member with member ID and issue date
- Return book and update status to Available
- Search book by ID or Title
- Track book issue history
- Display count of available and issued books
- Prevent issuing same book multiple times

### Non-Functional Requirements
- All operations within 30 seconds
- Support 10,000+ books in library
- Clear indication of book status
- Confirmation before issuing/returning
- Display issue date and expected return date

## Implementation Guidelines
1. Build using Python with Streamlit
2. Create separate tabs: Add Book, View Books, Issue Book, Return Book, Search
3. Use session state for data storage
4. Implement proper validation
5. Show book inventory statistics
6. Display issue/return history

## Deliverables
- Fully functional book management application
- Book inventory with status tracking
- Member issue/return functionality
- Search and filter capabilities
- Statistics dashboard

## Marks Distribution (Total: 20 marks)
- Book Management: 4 marks
- Issue Functionality: 4 marks
- Return Functionality: 4 marks
- Search & Filter: 3 marks
- Validation: 3 marks
- Statistics: 2 marks

---
**Time Limit:** 60 minutes
**Language:** Python (Streamlit)
