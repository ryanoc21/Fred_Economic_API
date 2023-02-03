import streamlit as st 
from backend import DataProcessing 

# Create the interactive elements of the graph 
st.title("Economic Data for Ireland 💶")
st.write("""
This interactive web app uses important Irish economic data that are taken from the Fred API
 https://fred.stlouisfed.org/docs/api/fred/. The data were written to converted to pandas dataframes and 
 written to csv files. 
""")

data_type = st.selectbox("Choose what data you want to view.",
                        ("Residential Property Prices", 
                        "Consumer Price Index (Inflation)",
                        "Unemployment Rates")
)

st.subheader(data_type) 

if data_type: 
    data = DataProcessing(data_type) 
    st.plotly_chart(data.plot_data()) 