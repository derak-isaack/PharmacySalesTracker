import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import pandas as pd
import duckdb
import os 

gc = gspread.service_account(filename='streamlit-422812-6887d646b099.json')

sh = gc.open('SalesTracker').sheet1  

data = pd.DataFrame(sh.get_all_values())

headers = data.iloc[0].tolist()  # Get first row as list

# Select the remaining data (excluding the header row)
data = data.iloc[1:]  # Get remaining rows

# Assign the headers to the DataFrame
data.columns = headers

# print(data)

db_file_path = 'sales2.duckdb'
if os.path.exists(db_file_path):
    os.remove(db_file_path)

conn = duckdb.connect(database=db_file_path)
conn.execute("CREATE TABLE sales_pharma (product STRING, quantity_sold INTEGER, price INTEGER, Date DATETIME, Name TEXT, Area TEXT, stock_remaining INTEGER)")
conn.execute("INSERT INTO sales_pharma SELECT * FROM data")