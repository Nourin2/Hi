import streamlit as st 
import pandas as pd 

#Sample sales data( replace main data source)

data = {
    'Product': ['Product A', 'Product B', 'Product C'],
    'Sales': [100, 250, 175],
    'Price': [20, 30, 15],
    'Date': pd.to_datetime(['2024-03-20', '2024-03-25', '2024-03-28'])
}

df = pd.DataFrame(data)

#Title and sidebar options
st.title ('Sales Dashboard')
selected_product = st.sidebar.selectbox('Select Product', df['Product'].unique())
selected_date = st.date_input('Select Data')  #Date = (df['Date'].min(), df['Date'].max()))


#Filter data based on selection 
filtered_df = df[
    (df['Product'] == selected_product) 
    #(df['Data'] >= date_range[0]) &
    #(df['Date'] <= date_range[1])
]

#Display metrics and table 
total_sales = filtered_df['Sales'].sum()
total_revenue = total_sales * filtered_df['Price'].iloc[0]

col1, col2 = st.columns(2)
with col1:
    st.metric('Total Sales', total_sales, delta=None)
    with col2:
        st.metric('Total Revenue', f'{total_revenue: .2f}', delta=None)
        
st.subheader('Sales Details')
st.dataframe (filtered_df)

#Add functionality for future sales tracking (form)
st.subheader('Record New Sale')

#Examle form with placeholders (replace with actual input fields)
new_product = st.text_input('Product Name')
new_sales = st.number_input('Sales Quantity')
new_price = st.number_input('Price per unit')

if st.button('Add Sale'):
    st.write('This functionality is not yet implemented')

    
#Implement logic to add new sale data


