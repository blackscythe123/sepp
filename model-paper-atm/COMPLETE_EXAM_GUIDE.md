# Complete Exam Structure Guide

## Exam Format: 3-Hour Scenario-Based Assessment

```
Part A: 15 marks  (30 minutes) → Requirements Identification
Part B: 20 marks  (30 minutes) → Design (DFD/Activity Diagrams)
Part C: 20 marks  (60 minutes) → Implementation (Simple Code)
Part D: 20 marks  (60 minutes) → Git/Tools/Version Control
Part E: 5 marks   (flexible)  → Learning Outcomes/Summary
─────────────────────────────
Total: 80 marks   (3 hours)
```

---

## PART A: Requirements Analysis (15 marks)

### What to Do:
1. **Read the given scenario carefully**
2. **Identify Functional Requirements** (What system DOES)
   - User operations: Add, View, Search, Update, Delete
   - Core business logic
   - Authentication/Security features
   - Data processing
   - At least 8-10 functional requirements

3. **Identify Non-Functional Requirements** (HOW system behaves)
   - Performance (time limits, response time)
   - Availability (24/7, business hours)
   - Scalability (number of records, users)
   - Security (authentication, validation)
   - Concurrency (single/multiple users)
   - Session management (timeouts)
   - Hardware/UI constraints
   - Data integrity
   - At least 10-15 non-functional requirements

### Format:
```
FUNCTIONAL REQUIREMENTS:
1. ...
2. ...
3. ...

NON-FUNCTIONAL REQUIREMENTS:
1. ...
2. ...
3. ...
```

### Tips:
- Be specific with constraints (e.g., "within 60 seconds" not just "fast")
- Don't mix functional and non-functional
- Use clear, concise language
- Reference specific parts of the scenario

---

## PART B: System Design (20 marks)

### What to Do:

#### Option 1: Data Flow Diagram (DFD)
Create **Level 0 or Level 1 DFD** showing:
- **External Entities** (Users, Operators, etc.)
- **Processes** (Main operations)
- **Data Stores** (Databases)
- **Data Flows** (Arrows showing data movement)

**Use proper DFD symbols:**
```
┌─────┐         ═════════      ●      ═══════════
│ Entity        Process       Data Store   Data Flow
│               (Bubble)       (Lines)     (Arrow)
└─────┘
```

#### Option 2: Activity Diagram
Show the **flow of one or two main operations:**
- Start/End
- Decision points (diamonds)
- Activities/Tasks (rectangles)  
- Swim lanes (optional, for actors)
- Flow arrows

**Example Activity:**
```
Start
  ↓
[Display Login Form]
  ↓
{Valid?} ──No──→ [Show Error] ──┐
  │ Yes                         │
  ↓                             │
[Process Request]               │
  ↓                             └──→ End
[Display Result]
  ↓
End
```

### Format:
- Use clear boxes and arrows
- Label all processes, entities, data stores
- Show data flowing into/out of processes
- Use legends if needed
- Draw neatly (can be hand-drawn or digital)

### Tips:
- DFD should match the functional requirements from Part A
- Show all major processes as separate bubbles
- Include all data stores (databases)
- Connect entities to processes
- One or two diagrams are sufficient (Level 0 + one detailed Level 1, OR just Level 1)

---

## PART C: Implementation (20 marks)

### What to Do:
Develop a **basic, working implementation** of ONE main operation from the scenario.

### Language Choice:
- **HTML + JavaScript (No CSS)** - Recommended for beginners
- **Streamlit (Python)** - Recommended for data/dashboard features

### Implementation Components:

1. **User Interface** (3-5 marks)
   - Input forms with clear labels
   - Output display (table, list, or message)
   - Buttons for actions
   - Clear navigation

2. **Core Functionality** (8-10 marks)
   - At least one full CRUD cycle
   - Data storage (in-memory, not database)
   - Basic search or filter
   - Validation of inputs
   - Error messages

3. **Code Quality** (3-5 marks)
   - Readable, well-organized code
   - Named variables meaningfully
   - Comments where needed
   - No unnecessary complexity

### Example Operations to Implement:
✓ Add record + View all
✓ Search by ID + Display details
✓ Filter by category + Count
✓ Update status + Log action
✓ Delete with confirmation

### What NOT to Include:
❌ Database integration
❌ Complex CSS styling (if using HTML)
❌ Login/Authentication complexity
❌ Multiple complex workflows
❌ Advanced features

### Suggested File Structure:
```
For HTML:
StudentManagementSystem/
  └── index.html (single file, all-in-one)

For Streamlit:
StudentManagementSystem/
  └── app.py (single file)
```

### Testing Before Submission:
- [ ] Forms work and accept input
- [ ] Validation messages display
- [ ] Data is stored correctly
- [ ] Search/Filter works
- [ ] Delete/Update works
- [ ] Output displays properly
- [ ] No JavaScript/Python errors
- [ ] Code is readable

---

## PART D: Git/Tools & Version Control (20 marks)

### What to Do:

1. **Create a Git Repository**
   - Initialize git: `git init`
   - Add all files: `git add .`
   - Make initial commit: `git commit -m "Initial commit"`

2. **Show Git History**
   - Show commit log: `git log`
   - Show detailed changes: `git log -p`
   - Show branch information: `git branch -a`

3. **Demonstrate Branching (If Applicable)**
   - Create feature branch: `git checkout -b feature/add-student`
   - Make changes
   - Commit changes
   - Note the branch names

4. **Understanding of Tools** (As asked in exam):
   - Version control workflow
   - Commit messages (should be meaningful)
   - Branch naming conventions
   - Why use version control
   - MLflow basics (if mentioned - just log parameters/metrics)
   - Optuna basics (if mentioned - just understand hyperparameter tuning)

### Key Git Commands to Know:
```bash
git init                    # Initialize repository
git add <file>             # Stage changes
git commit -m "message"    # Create commit
git log                    # View history
git branch                 # List branches
git checkout -b <name>     # Create new branch
git status                 # Check status
git diff                   # See what changed
```

### What to Show in Exam:
- Repository initialized with meaningful commits
- Use descriptive commit messages (Not "xyz" or "update")
- Show understanding of version control concepts
- Explain WHY version control is important
- If using branches, show how development works

### Commit Message Format:
```
Good:
✓ "Add student search functionality"
✓ "Fix validation in add form"
✓ "Update database schema"

Bad:
❌ "update"
❌ "fix bug"
❌ "working code"
```

---

## PART E: Learning Outcomes & Summary (5 marks)

### What to Write:
A brief summary (1-2 pages) covering:

1. **Understanding of Requirements Analysis**
   - What you learned about identifying functional vs non-functional requirements
   - How requirements guide system design

2. **System Design Insights**
   - How DFD represents system flow
   - How activity diagrams show user interactions
   - Importance of proper design before coding

3. **Implementation Experience**
   - Challenges faced during coding
   - What went well
   - What you learned about building systems

4. **Tool Usage Understanding**
   - Git workflow and its importance
   - How version control helps in team projects
   - Any other tools used (MLflow, Optuna concepts)

5. **Practical Applications**
   - Where these concepts apply in real projects
   - How this will help in career

### Format:
```
Learning Outcomes

1. Requirements Analysis
   - Identified 12 functional requirements
   - Understood NF requirements importance
   - Learned separation of concerns

2. System Design
   - Created DFD showing system flow
   - Activity diagram showed user operations
   - Design helped in implementing correctly

3. Implementation Challenges
   - Form validation was tricky, solved by...
   - Data storage managed using...

4. Tool Learning
   - Learned Git branching strategy
   - Understood importance of meaningful commits

5. Real-World Application
   - These concepts apply to...
   - In real projects, we would...
```

---

## Complete Exam Flow Summary

```
┌─────────────────────────────────────────────┐
│ Read Scenario (5 minutes)                   │
│ Understand what's being asked               │
└──────────┬──────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│ PART A: Requirements (30 minutes)           │
│ • Extract Functional Requirements           │
│ • Extract Non-Functional Requirements       │
│ • List 8-10 of each                        │
└──────────┬──────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│ PART B: Design (30 minutes)                │
│ • Draw DFD (Level 0 or 1)                  │
│ • Draw Activity Diagram for 1-2 operations │
│ • Show system flow clearly                 │
└──────────┬──────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│ PART C: Implementation (60 minutes)         │
│ • Develop HTML or Streamlit app            │
│ • Implement basic CRUD                     │
│ • Test thoroughly                          │
│ • Make sure it works!                      │
└──────────┬──────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│ PART D: Git/Tools (60 minutes)             │
│ • Initialize repository                    │
│ • Make meaningful commits                  │
│ • Show branching (if applicable)           │
│ • Demonstrate version control              │
└──────────┬──────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│ PART E: Summary (Flexible)                 │
│ • Write learning outcomes                  │
│ • Explain what you learned                 │
│ • Mention applications                     │
└─────────────────────────────────────────────┘
```

---

## Final Exam Tips

### Do's ✓
✓ Read the scenario CAREFULLY (it has all clues)
✓ Write CLEARLY (examiners need to read your work)
✓ Show your UNDERSTANDING, not just code
✓ Use PROPER TERMINOLOGY (Functional, Non-Functional, DFD, etc.)
✓ Make your implementation WORK first, then optimize
✓ Use meaningful Git commit messages
✓ Keep code SIMPLE and READABLE
✓ Show ERROR HANDLING in implementation
✓ Manage TIME effectively (don't spend 2 hours on Part C)

### Don'ts ❌
❌ Don't overcomplicate requirements analysis
❌ Don't draw poorly labeled diagrams
❌ Don't build an over-engineered implementation
❌ Don't forget to test your code
❌ Don't write meaningless commit messages
❌ Don't use complex styling (if using HTML)
❌ Don't ignore validation/error handling
❌ Don't run out of time (allocate 30-30-60 for Parts A-B-C)

---

## Success Checklist

Before submitting:

Part A:
- [ ] Listed at least 8 functional requirements
- [ ] Listed at least 10 non-functional requirements
- [ ] Requirements are specific and clear
- [ ] Properly separated into categories

Part B:
- [ ] DFD includes all entities, processes, data stores
- [ ] Arrows show data flow direction
- [ ] All labels are clear
- [ ] OR Activity diagram shows decision points and activities

Part C:
- [ ] Code runs without errors
- [ ] At least one CRUD operation works
- [ ] Input validation present
- [ ] User-friendly interface
- [ ] Code is readable and commented

Part D:
- [ ] Git repository initialized
- [ ] At least 3-5 meaningful commits
- [ ] Commits show incremental development
- [ ] Can explain git branching

Part E:
- [ ] Brief summary of learning
- [ ] Mentions key concepts learned
- [ ] Shows understanding of practical applications

Good luck! You've got this! 🎯
