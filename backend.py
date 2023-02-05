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
            "Consumer Price Index 💶": "IRL_CPI.csv",
            "Residential Property Prices 🏠": "IRL_Property.csv",
            "Unemployment Rates 📈": "IRL_Unemployment_Rate.csv"
        }

        #self.df = pd.read_csv(f'{self.files.get(self.user_choice)}')
    def read_data(self):
        df = pd.read_csv(f'{self.files.get(self.user_choice)}')
        return df 
    
    def plot_data(self):
        """
        Plot the read csv data on a graph. 
        """
        Timeframe = self.read_data()
        Timeframe = Timeframe['Timeframe']
        Eco_data = self.read_data() 
        Eco_data = Eco_data['Data'] 

        # Plot line graph 
        fig = px.line(x=Timeframe,y=Eco_data)

        return fig 