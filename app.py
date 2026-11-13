
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AVLODHANA",
    page_icon="💡",
    layout="wide"
)

st.title("💡 AVLODHANA")
st.subheader("Smart Business Management System")

st.write(
    "AVLODHANA is a smart business management "
    "application designed to manage customers, "
    "track business activities and analyse performance."
)

# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox(
    "Choose an option",
    ["Dashboard", "Add Customer", "Customer Records", "About"]
)

# Customer storage
if "customers" not in st.session_state:
    st.session_state.customers = []

# Dashboard
if menu == "Dashboard":

    st.header("Business Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", len(st.session_state.customers))
    col2.metric("System Status", "Active")
    col3.metric("Today's Date", datetime.now().strftime("%d-%m-%Y"))

    st.success("Welcome to AVLODHANA!")

# Add Customer
elif menu == "Add Customer":

    st.header("Add New Customer")

    name = st.text_input("Customer Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    business = st.text_input("Business Name")

    if st.button("Save Customer"):

        if name and email and phone and business:

            customer = {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Business": business
            }

            st.session_state.customers.append(customer)

            st.success("Customer added successfully!")

        else:
            st.warning("Please fill all the fields.")

# Customer Records
elif menu == "Customer Records":

    st.header("Customer Records")

    if st.session_state.customers:

        df = pd.DataFrame(st.session_state.customers)

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Customer Records",
            csv,
            "customers.csv",
            "text/csv"
        )

    else:
        st.info("No customer records available.")

# About
elif menu == "About":

    st.header("About AVLODHANA")

    st.write("""
    AVLODHANA is a business management project
    developed using Python and Streamlit.

    Features:
    - Customer management
    - Business dashboard
    - Customer record tracking
    - CSV data export

    Technology Used:
    - Python
    - Streamlit
    - Pandas
    """)

st.divider()

st.caption("© 2026 AVLODHANA | Smart Business Management System")
