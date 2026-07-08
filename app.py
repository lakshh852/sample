import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="Attendance Management System",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Attendance Management System")

students = [
    "Arun",
    "Bala",
    "Karthik",
    "Priya",
    "Riya"
]

today = datetime.now().strftime("%d-%m-%Y")

st.write("### Date:", today)

attendance = []

st.write("### Mark Attendance")

for student in students:
    status = st.radio(
        student,
        ["Present", "Absent"],
        horizontal=True,
        key=student
    )

    attendance.append([today, student, status])

if st.button("Save Attendance"):

    df = pd.DataFrame(
        attendance,
        columns=["Date", "Student Name", "Status"]
    )

    if os.path.exists("attendance.csv"):
        old_df = pd.read_csv("attendance.csv")
        df = pd.concat([old_df, df], ignore_index=True)

    df.to_csv("attendance.csv", index=False)

    st.success("Attendance Saved Successfully!")

if os.path.exists("attendance.csv"):

    st.write("## Attendance Records")

    data = pd.read_csv("attendance.csv")

    st.dataframe(data)

    csv = data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Attendance CSV",
        data=csv,
        file_name="attendance.csv",
        mime="text/csv"
    )
