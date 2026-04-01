import streamlit as st

st.title("Event Management System")

if 'events' not in st.session_state:
    st.session_state.events = []
if 'participants' not in st.session_state:
    st.session_state.participants = []

tab1, tab2, tab3 = st.tabs(["Events", "Register", "Participants"])

with tab1:
    st.subheader("Create Event")
    event_id = st.text_input("Event ID", key="eveid")
    event_name = st.text_input("Event Name", key="evename")
    event_date = st.date_input("Event Date", key="evedate")
    event_venue = st.text_input("Venue", key="evevenue")
    event_capacity = st.number_input("Capacity", min_value=1, key="evecap")
    
    if st.button("Create Event"):
        if event_id and event_name:
            st.session_state.events.append({
                'id': event_id,
                'name': event_name,
                'date': str(event_date),
                'venue': event_venue,
                'capacity': event_capacity,
                'registrations': 0
            })
            st.success("Event created!")
        else:
            st.error("Fill required fields")
    
    st.subheader("Events")
    if st.session_state.events:
        for idx, event in enumerate(st.session_state.events):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{event['name']}** (ID: {event['id']})")
                st.write(f"Date: {event['date']} | Venue: {event['venue']}")
                st.write(f"Registrations: {event['registrations']}/{event['capacity']}")
            with col2:
                if st.button("Delete", key=f"del_eve_{idx}"):
                    st.session_state.events.pop(idx)
                    st.rerun()
    else:
        st.info("No events created")

with tab2:
    st.subheader("Register for Event")
    if st.session_state.events:
        available_events = [e for e in st.session_state.events if e['registrations'] < e['capacity']]
        
        if available_events:
            event_id = st.selectbox("Select Event", [e['id'] for e in available_events])
            reg_name = st.text_input("Participant Name", key="regname")
            reg_email = st.text_input("Email", key="regemail")
            
            if st.button("Register"):
                if reg_name and reg_email:
                    participant = {
                        'eventId': event_id,
                        'name': reg_name,
                        'email': reg_email,
                        'regDate': str(st.date_input("Today"))
                    }
                    st.session_state.participants.append(participant)
                    
                    for event in st.session_state.events:
                        if event['id'] == event_id:
                            event['registrations'] += 1
                    
                    st.success("Registered successfully!")
                    st.rerun()
                else:
                    st.error("Fill all fields")
        else:
            st.warning("No events with available capacity")
    else:
        st.warning("No events available")

with tab3:
    st.subheader("Registered Participants")
    if st.session_state.participants:
        for idx, part in enumerate(st.session_state.participants):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"**{part['name']}** ({part['email']})")
                st.write(f"Event ID: {part['eventId']} | Registered: {part['regDate']}")
            with col2:
                if st.button("Remove", key=f"rem_part_{idx}"):
                    event_id = part['eventId']
                    for event in st.session_state.events:
                        if event['id'] == event_id:
                            event['registrations'] -= 1
                    st.session_state.participants.pop(idx)
                    st.rerun()
    else:
        st.info("No participants registered yet")
