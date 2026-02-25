import streamlit as st
import pandas as pd

st.title("Recruiting App")

# --- SESSION STATE SETUP ---
fields = ["full_name", "age", "field", "phone", "email", "skills", "decision"]
for field in fields:
    if field not in st.session_state:
        st.session_state[field] = "" if field != "decision" else "Accepted"

# --- FORM ---
with st.form("application_form"):

    st.session_state.full_name = st.text_input("Full Name", st.session_state.full_name)
    st.session_state.age = st.text_input("Age", st.session_state.age)
    st.session_state.field = st.text_input("Field of study", st.session_state.field)
    st.session_state.phone = st.text_input("Phone number", st.session_state.phone)
    st.session_state.email = st.text_input("Email", st.session_state.email)
    st.session_state.skills = st.text_input("Skills", st.session_state.skills)
    st.session_state.decision = st.selectbox(
        "Decision", ["Accepted", "Rejected", "Pending"],
        index=["Accepted","Rejected","Pending"].index(st.session_state.decision)
    )

    submitted = st.form_submit_button("Submit Application")

# --- SUBMIT DATA ---
if submitted:
    file_name = st.session_state.full_name.strip().lower().replace(" ", "_") + ".csv"

    columns = [
        "Full Name", "Age", "Field of study",
        "Phone number", "Email", "Skills", "Decision"
    ]

    data = [[
        st.session_state.full_name,
        st.session_state.age,
        st.session_state.field,
        st.session_state.phone,
        st.session_state.email,
        st.session_state.skills,
        st.session_state.decision
    ]]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv(file_name, index=False, sep=';')

    st.success(f"Application saved as {file_name}")

    # Download button
    with open(file_name, "rb") as file:
        st.download_button(
            label="Download Applicant File",
            data=file,
            file_name=file_name,
            mime="text/csv"
        )

    # Reset form fields after submit
    for field in fields:
        st.session_state[field] = "" if field != "decision" else "Accepted"

# --- NEW APPLICANT BUTTON ---
if st.button("New Applicant"):
    # Reset all form fields immediately
    for field in fields:
        st.session_state[field] = "" if field != "decision" else "Accepted"