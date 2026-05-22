import streamlit as st
from summariser import generate_meeting_minutes


st.set_page_config(page_title="Meeting Minutes Generator", page_icon="📝")

st.title("Meeting Minutes Generator")

meeting_notes = st.text_area("Enter raw meeting notes here:", height=300)

if st.button("Generate Meeting Minutes"):
    if not meeting_notes.strip():
        st.warning("Please enter some meeting notes before generating minutes.")
    else:
        with st.spinner("Generating meeting minutes..."):
            result = generate_meeting_minutes(meeting_notes)
            if result["success"]:
                minutes = result["data"]
                st.subheader("Generated Meeting Minutes")
                st.write(minutes.summary)

                st.subheader("Agenda Items")
                for item in minutes.agenda_items:
                    st.markdown(f"- {item}")

                st.subheader("Decisions Made")
                for decision in minutes.decisions:
                    st.markdown(f"- {decision.decision} (Owner: {decision.owner})") 
                
                st.subheader("Action Items")
                for action in minutes.action_items:
                    st.markdown(f"- {action.task} (Owner: {action.owner}, Due: {action.due_date})")

                st.subheader("Next Meeting")
                st.write(minutes.next_meeting)