# PROJECT MANAGEMENT SYSTEM - Exam Question

## Scenario
A company needs a project management system to manage projects and track tasks. Project managers should be able to create projects, assign tasks, track progress, and generate reports.

## Requirements

### Functional Requirements
- Create project with ID, Name, Manager, Deadline
- View all active projects with status
- Add tasks to projects with Task Name and Assignee
- Track task status (Pending/In Progress/Completed)
- Update project progress percentage
- Search projects by ID or Name
- Display project-task hierarchy
- Generate project completion report

### Non-Functional Requirements
- Operations within 30 seconds
- Support 1000+ concurrent projects
- Real-time task update
- Progress calculation accuracy
- Deadline tracking

## Implementation Guidelines
1. Build using Python with Streamlit
2. Sections: Create Project, View Projects, Add Task, Track Progress, Reports
3. Store project and task data using session state
4. Implement task-project relationship
5. Calculate project progress based on tasks
6. Track deadlines and completion dates

## Deliverables
- Project creation and management system
- Task assignment and tracking
- Progress percentage calculation
- Project-task hierarchy view
- Deadline management
- Completion reporting
- Search and filter projects

## Marks Distribution (Total: 20 marks)
- Project Management: 3 marks
- Task Assignment: 4 marks
- Progress Calculation: 4 marks
- Status Update: 3 marks
- Search & Filter: 3 marks
- Validation: 3 marks

---
**Time Limit:** 60 minutes
**Language:** Python (Streamlit)
