
import pandas as pd
import streamlit as st


# Read the Excel file and select the desired sheet
excel_file = pd.ExcelFile("SPXDATA.xlsx")
sheet_name = "GEX"  # Replace with the name of your sheet
df = pd.read_excel(excel_file, sheet_name)

# Create a Streamlit app
st.title("SPX GEX")
st.dataframe(df)  # Display the data in a table

st.bar_chart(
    df,
    x="STRIKE",
    y=["Sum of GEX CALLS ", "Sum of GEX PUTS"],  # <-- You can pass multiple columns!
)



# Read the Excel file and select the desired sheet
excel_file = pd.ExcelFile("SPXDATA.xlsx")
sheet_name = "OPEN INTEREST"  # Replace with the name of your sheet
df = pd.read_excel(excel_file, sheet_name)

# Create a Streamlit app
st.title("SPX OI ")
st.dataframe(df)  # Display the data in a table

st.bar_chart(
    df,
    x="STRIKE",
    y=["Sum of Open.Int Calls", "Sum of Open.Int  Puts"],  # <-- You can pass multiple columns!
)
