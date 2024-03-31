import streamlit as st
from datetime import date

# Sample employee data (replace with your data source)
employees = [
    {"name": "John Doe", "department": "Sales", "status": None},
    {"name": "Jane Smith", "department": "Marketing", "status": None},
    {"name": "Mike Jones", "department": "Engineering", "status": None},
]

# Title and date selection
st.title("Employee Attendance Tracker")
today = date.today()
st.write(f"Date: {today.strftime('%Y-%m-%d')}")

# Function to update employee status
def update_status(employee_index, new_status):
    employees[employee_index]["status"] = new_status

# Display employee information with status selection
for i, employee in enumerate(employees):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{employee['name']} ({employee['department']})")
    with col2:
        status_options = ["Absent", "Present"]
        selected_status = st.selectbox("Status", status_options, key=i)
        if st.button("Update", key=f"update_{i}"):
            update_status(i, selected_status)

# Display updated employee data
st.subheader("Attendance Summary")
st.dataframe(employees)