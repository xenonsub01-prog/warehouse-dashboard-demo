import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ---------------- CONFIG -----------------
DATA_DIR = "data"
ORDERS_FILE = os.path.join(DATA_DIR, "orders.csv")
LOOKUPS_FILE = os.path.join(DATA_DIR, "lookups.csv")
LOG_FILE = os.path.join(DATA_DIR, "log.csv")

OWNER_KEY = "admin12345"

# ---------------- HELPERS -----------------
def load_orders():
    if os.path.exists(ORDERS_FILE):
        return pd.read_csv(ORDERS_FILE)
    return pd.DataFrame(columns=["OrderID","OrderDate","Warehouse","Customer","SKU","Qty","Status","Priority","InvoiceNo","UpdatedBy","UpdatedAt"])

def save_orders(df):
    df.to_csv(ORDERS_FILE, index=False)

def load_lookups():
    if os.path.exists(LOOKUPS_FILE):
        return pd.read_csv(LOOKUPS_FILE)
    return pd.DataFrame(columns=["Status","Priority"])

# ---------------- APP -----------------
query_params = st.experimental_get_query_params()
admin_key = query_params.get("admin", [""])[0]

if admin_key == OWNER_KEY:
    st.sidebar.success("Authorized: owner")
    st.title("Owner — Warehouse Orders (Demo)")

    df = load_orders()
    if not df.empty:
        st.metric("Open", int((df["Status"]=="Open").sum()))
        st.metric("Invoiced", int((df["Status"]=="Invoiced").sum()))
        st.write("Orders Table")
        st.dataframe(df)
    else:
        st.info("No orders found.")

else:
    st.sidebar.error("Access denied. Invalid or expired token.")
