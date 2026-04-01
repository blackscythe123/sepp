# EVENT MANAGEMENT SYSTEM - Exam Question

## Scenario
An organization needs an event management system to organize events and manage participant registrations. Event managers should be able to create events, register participants, and generate attendance reports.

## Requirements

### Functional Requirements
- Create event with ID, Name, Date, Venue, Capacity
- Display all events with registration count
- Register participant with Name, Email, Phone
- Check event availability (prevent overbooking)
- Cancel participant registration
- Search events by ID or Date
- Display participant list for each event
- Generate attendance report

### Non-Functional Requirements
- Operations within 30 seconds
- Support 500+ concurrent events
- Real-time registration updates
- Prevent overbooking
- Email format validation

## Implementation Guidelines
1. Build using Python with Streamlit
2. Sections: Create Event, View Events, Register Participant, Participant List, Reports
3. Store event and participant data using session state
4. Implement capacity checking
5. Track registration date and time
6. Generate attendance statistics

## Deliverables
- Event creation and management system
- Participant registration system
- Capacity management and overbooking prevention
- Participant list per event
- Search and filter events
- Attendance reporting
- Registration confirmation tracking

## Marks Distribution (Total: 20 marks)
- Event Management: 3 marks
- Participant Registration: 4 marks
- Capacity Management: 3 marks
- Participant Tracking: 3 marks
- Attendance Reporting: 4 marks
- Validation: 3 marks

---
**Time Limit:** 60 minutes
**Language:** Python (Streamlit)
