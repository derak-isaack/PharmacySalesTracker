import streamlit as st 
from streamlit_gsheets import GSheetsConnection
import pandas as pd 

st.set_page_config(page_title="Sales Tracker", page_icon=":bar_chart:")
st.title("🚑Pharmacy Sales📊📈 Tracker:")
st.image("Health.jpg", width=200, caption="Pharmacy", use_column_width=True)

url = 'https://docs.google.com/spreadsheets/d/1UdYbvLGmMvyaH3fdT84_NYFO_jY8DMHWdsbaAiUZDQU/edit?usp=sharing'

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, sheet_name='Pharmaflow', usecols=list(range(7)))

# st.write(df)
PRODUCTS = [
    "Capsules",
    "Tablets",
    "Injections",
    "Syrups",
    "Creams",
    "Ointments",
    "Suppositories",
    "Others"
]

col2 = st.columns([2, 3])  # Adjust column widths as needed

# Column 1 - Image
# with col1:
#     st.image("tablet.jpg", width=300, caption="Pharmacy", use_column_width=True)

# st.sidebar.header("Pharmacy Sales Tracker") 
st.sidebar.markdown("This is a pharmacy sales tracker application")
with st.form("Pharmacy sale form"):
    product_sold = st.sidebar.selectbox("Select Product", options=PRODUCTS)
    quantity_sold = st.sidebar.number_input("Enter Quantity sold")
    item_price = st.sidebar.number_input("Enter Price")
    date = st.sidebar.date_input("Enter Date")
    Name = st.sidebar.text_input("Enter Name")
    area_name = st.sidebar.text_input("Enter Area Name")
    remainder = st.sidebar.number_input("Enter Remaining stock")
        
    st.sidebar.markdown("**Required**")
        
        
    submit_button = st.form_submit_button("Submit")
        
        
    if submit_button:
        if not product_sold:
            st.error("Please select a product")
            st.stop()
        else:
            sale_data = pd.DataFrame(
                [
                {
                "product": product_sold, 
                "quantity sold": quantity_sold, 
                "price": item_price, 
                "Date": date, 
                "Name": Name, 
                "Area": area_name, 
                "stock remaining": remainder
                }
                ])
            updated_df = pd.concat([df, sale_data], ignore_index=True)
            conn.update(data=sale_data)
            st.success("Data saved successfully")
            
    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)

    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")