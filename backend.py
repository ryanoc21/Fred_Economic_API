"""
This file contains the code for the clas that will perform the backend functionality of the project. 
It contains methods that will read data from the API and plot time series graphs using plotly. 
"""

import pandas as pd 
import plotly.express as px


class DataProcessing: 

    def __init__(self,user_choice):
        self.user_choice = user_choice 

        # Store the relevant user choices and file names 
        self.files = {
            "Consumer Price Index (Inflation)": "IRL_CPI.csv",
            "Residential Property Prices": "IRL_Property.csv",
            "Unemployment Rates": "IRL_Unemployment_Rate.csv"
        }


    def plot_data(self):
        """
        Read the data from the csv files, and plot the on a line graph. 
        """
        # Read to dataframe 
        df = pd.read_csv(f'{self.files.get(self.user_choice)}')

        # Plot line graph 
        fig = px.line(x=df['Timeframe'],y=[df['Data']])

        return fig 



        # Note: The graphs are all plotting on top of one another so you will need to fix that. 
        # The graphs also need tidying up. 
        # See if you can add a feature that will allow the user to zoom in and out on the graph. 