import streamlit as st

st.title("Hospital Management System")

if 'patients' not in st.session_state:
    st.session_state.patients = []

tab1, tab2, tab3 = st.tabs(["Register Patient", "Patient Records", "Search"])

with tab1:
    st.subheader("Register Patient")
    patient_id = st.text_input("Patient ID", key="hpid")
    patient_name = st.text_input("Patient Name", key="hpname")
    patient_age = st.number_input("Age", min_value=0, key="hpage")
    patient_disease = st.text_input("Disease/Condition", key="hpdisease")
    patient_doctor = st.text_input("Assigned Doctor", key="hpdoctor")
    
    if st.button("Register Patient"):
        if patient_id and patient_name:
            st.session_state.patients.append({
                'id': patient_id,
                'name': patient_name,
                'age': patient_age,
                'disease': patient_disease,
                'doctor': patient_doctor,
                'status': 'Admitted'
            })
            st.success("Patient registered successfully!")
        else:
            st.error("Please fill required fields")

with tab2:
    st.subheader("Patient Records")
    if st.session_state.patients:
        for idx, patient in enumerate(st.session_state.patients):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{patient['name']}** (ID: {patient['id']})")
                st.write(f"Age: {patient['age']} | Disease: {patient['disease']} | Doctor: {patient['doctor']} | Status: {patient['status']}")
            with col2:
                if st.button("Delete", key=f"del_patient_{idx}"):
                    st.session_state.patients.pop(idx)
                    st.rerun()
        
        st.subheader("Update Patient Status")
        patient_id = st.selectbox("Select Patient", [p['id'] for p in st.session_state.patients])
        new_status = st.selectbox("New Status", ["Admitted", "Under Treatment", "Discharged", "Critical"])
        
        if st.button("Update Status"):
            for patient in st.session_state.patients:
                if patient['id'] == patient_id:
                    patient['status'] = new_status
                    st.success("Status updated!")
                    st.rerun()
    else:
        st.info("No patients registered yet")

with tab3:
    st.subheader("Search Patient")
    search_id = st.text_input("Enter Patient ID to search")
    if st.button("Search Patient"):
        result = [p for p in st.session_state.patients if p['id'] == search_id]
        if result:
            patient = result[0]
            st.success("Patient Found!")
            st.write(f"**ID:** {patient['id']}")
            st.write(f"**Name:** {patient['name']}")
            st.write(f"**Age:** {patient['age']}")
            st.write(f"**Disease/Condition:** {patient['disease']}")
            st.write(f"**Doctor:** {patient['doctor']}")
            st.write(f"**Status:** {patient['status']}")
        else:
            st.warning("Patient not found")
