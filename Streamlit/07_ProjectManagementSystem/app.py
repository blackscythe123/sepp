import streamlit as st

st.title("Project Management System")

if 'projects' not in st.session_state:
    st.session_state.projects = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

tab1, tab2, tab3 = st.tabs(["Projects", "Tasks", "Overview"])

with tab1:
    st.subheader("Create Project")
    proj_id = st.text_input("Project ID", key="projid")
    proj_name = st.text_input("Project Name", key="projname")
    proj_manager = st.text_input("Project Manager", key="projmgr")
    proj_deadline = st.date_input("Deadline", key="projdate")
    
    if st.button("Create Project"):
        if proj_id and proj_name:
            st.session_state.projects.append({
                'id': proj_id,
                'name': proj_name,
                'manager': proj_manager,
                'deadline': str(proj_deadline),
                'status': 'Active',
                'progress': 0
            })
            st.success("Project created!")
        else:
            st.error("Fill required fields")
    
    st.subheader("Active Projects")
    if st.session_state.projects:
        for idx, proj in enumerate(st.session_state.projects):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{proj['name']}** (ID: {proj['id']})")
                st.write(f"Manager: {proj['manager']} | Deadline: {proj['deadline']} | Progress: {proj['progress']}%")
            with col2:
                if st.button("Delete", key=f"del_proj_{idx}"):
                    st.session_state.projects.pop(idx)
                    st.rerun()
    else:
        st.info("No projects created")

with tab2:
    st.subheader("Add Task")
    if st.session_state.projects:
        proj_id = st.selectbox("Select Project", [p['id'] for p in st.session_state.projects])
        task_name = st.text_input("Task Name", key="taskname")
        task_assignee = st.text_input("Assigned To", key="taskassign")
        
        if st.button("Add Task"):
            task = {
                'projectId': proj_id,
                'name': task_name,
                'assignee': task_assignee,
                'status': 'Pending'
            }
            st.session_state.tasks.append(task)
            st.success("Task added!")
            st.rerun()
    else:
        st.warning("Create a project first")
    
    st.subheader("Tasks")
    if st.session_state.tasks:
        for idx, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{task['name']}** (Project: {task['projectId']})")
                st.write(f"Assigned to: {task['assignee']} | Status: {task['status']}")
            with col2:
                if st.button("Complete", key=f"comp_task_{idx}"):
                    task['status'] = 'Completed'
                    st.rerun()
    else:
        st.info("No tasks added")

with tab3:
    st.subheader("Project Overview")
    if st.session_state.projects:
        st.write(f"**Total Projects:** {len(st.session_state.projects)}")
        st.write(f"**Total Tasks:** {len(st.session_state.tasks)}")
        
        completed_tasks = len([t for t in st.session_state.tasks if t['status'] == 'Completed'])
        st.write(f"**Completed Tasks:** {completed_tasks}")
    else:
        st.info("No data to show")
