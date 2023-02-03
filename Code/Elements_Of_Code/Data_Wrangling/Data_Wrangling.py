#importing libraries
#code is designed to run in colab
#1 file is required to run this code
#found in: CSV files -> Hard-Coded_CSVs -> 1.csv

import requests
import pandas as pd
import time
import numpy as np
import json
import plotly.express as px
import plotly.io as pio
import numpy as np

#Data wrangling
#--------------------------------------------------------------------------------------------
#Dataframe creating a random column full of nothing
maindfs=maindf.drop("")
main_csv = maindfs.to_csv('main_data.csv')
#transposing data set so it can be transposed with demographic data
maindft = maindfs.transpose() 
#Converting strings to integers
maindft[['bicycle-theft','burglary','criminal-damage-arson','drugs','other-crime','other-theft','possession-of-weapons','public-order','robbery','shoplifting','theft-from-the-person','vehicle-crime','violent-crime']] = maindft[['bicycle-theft','burglary','criminal-damage-arson','drugs','other-crime','other-theft','possession-of-weapons','public-order','robbery','shoplifting','theft-from-the-person','vehicle-crime','violent-crime']].apply(pd.to_numeric)

#Placing borough as the first column to get the intended merge effect
firstcolumn=maindft.pop('Borough')
maindft.insert(0, "Borough", firstcolumn)
maindft.style.hide_index()

#Opening csv with demographic and income data
df2 = pd.read_csv('1.csv')
#Creating a total crime column in the dataframe
df2['Total Crime'] = TCF
#Converting string values to numerical calues
df2[['Median Income', 'House Price', 'Years to Purchase a House on Median Income','Population','Area','Population density']] = df2[['Median Income', 'House Price', 'Years to Purchase a House on Median Income','Population','Area','Population density']].apply(pd.to_numeric)
#Creating Column with crime rate
df2['Crime Rate']=(df2['Total Crime']/df2['Population'])*100
#Merging dataframes so that data is all in the same place for visualisation
df3=pd.merge(maindft, df2, on="Borough")