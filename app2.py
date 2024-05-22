import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Tracker", page_icon=":bar_chart:")
st.title("🚑Pharmacy Sales📊📈 Tracker:")
st.image("Health.jpg", width=200, caption="Pharmacy", use_column_width=True)

# Authenticate with Google and read the secret JSON file
scope = [
    "https://www.googleapis.com/auth/spreadsheets",  
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file('streamlit-422812-6887d646b099.json', scopes=scope)  

# Authorize and access the spreadsheet
client = gspread.authorize(creds)
sh = client.open('SalesTracker').worksheet('Pharmaflow')  

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

role = st.sidebar.radio("Select Role", ("Regular User", "Supervisor"))

if role == "Regular User":
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
                date_str = date.strftime("%Y-%m-%d")
                # Append user input to Google Sheets
                row = [product_sold, quantity_sold, item_price, date_str, Name, area_name, remainder]
                sh.append_row(row)
                st.success("Data saved successfully")


else:
    # Supervisor role: Display entire dataframe
    df = pd.DataFrame(sh.get_all_records())
    st.write(df)            
    
