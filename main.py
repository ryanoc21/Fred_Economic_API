import streamlit as st 
from backend import DataProcessing 

#ย Create the interactive elements of the graph 
st.title("Economic Data for Ireland ๐ฎ๐ช")
st.write("""
This interactive web app uses important Irish economic data that are taken from the Fred API
 https://fred.stlouisfed.org/docs/api/fred/. The data were converted to pandas dataframes and 
 written to csv files. 
""")

data_type = st.selectbox("Choose what data you want to view.",
                        ("Residential Property Prices ๐ ", 
                        "Unemployment Rates ๐",
                        "Consumer Price Index ๐ถ")
)

st.subheader(data_type) 

if data_type: 
    data = DataProcessing(data_type) 
    st.plotly_chart(data.plot_data()) 