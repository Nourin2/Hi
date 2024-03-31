import streamlit as st 

employees = [
    {'name': 'John Doe', 'department': 'Sales', 'Job_title': 'Sales Manager'},
    {'name': 'Jane Smith', 'department': 'Mareketing', 'job_title': 'Marketing '},
    {'name': 'Mike Jones', 'department': 'Engineering', 'job_title': 'Software Engineer'}
]

# Title and sidebar selection 
st.title('HR Employee Information')
selected_department = st.sidebar.selectbox('Select Department',set(emp['department'] for emp in employees))

#Filtered employee based on selection 
filtered_employees = [emp for emp in employees if emp['department']==selected_department]

#Display employee information table 
if filtered_employees:
    st.subheader ('Employees')
    st.dataframe (filtered_employees)
else:
    st.write('No employees is found in', selected_department)
    
#add functionality based on my needs 

if st.button ('Request Time off'):
    st.write('This functionality is not yet development')
