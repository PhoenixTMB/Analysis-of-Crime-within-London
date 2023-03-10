#These plots have been set up to run in colab as can be seen in line 11
#Importing libraries
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
import matplotlib.pyplot as plt
pio.renderers.default = 'colab'
import plotnine
from plotnine import *


                #Setting up for choropleth maps
#----------------------------------------------------------------------------------------------------------------------------

#Create Dictionary for Mapping
map_boroughs = {}
#Open geojson file with borough boundaries
boundaries = json.load(open('2.json', 'r'))

#Create dictionary for mapping part 2
for feature in boundaries['features']: 
  feature['id']=feature['properties']['id']
  map_boroughs[feature['properties']['name']]=feature['id']

#Creatinga dataframe column which applies the area IDs to the relative areas
df3['id'] = df3['Borough'].apply(lambda x:map_boroughs[(x)])


       #PLOTS - Choropleth maps
#Showing total crime in each borough 
def figure1():
          fig1 = px.choropleth(df3,
                              locations='id', 
                              geojson=boundaries, 
                              color='Total Crime', 
                              hover_name ='Borough',
                              scope='europe',
                              title="Total Crime Chloropleth",
                              color_continuous_scale=px.colors.diverging.RdYlGn,
                              color_continuous_midpoint=1500)
          fig1.update_geos(fitbounds='locations', visible=False)

          fig1.write_html("output.html", full_html=False, include_plotlyjs='cdn')
          fig1.write_image("TotalCrimeChoropleth.png")
#Showing bicycle theft in each borough 
def figure2(): 
  fig3 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='bicycle-theft', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Bicycle Theft Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=60)
  fig3.update_geos(fitbounds='locations', visible=False)
  fig3.write_image("BicycleTheftChoropleth.png")
#Showing drug crime in each borough
def figure3(): 
  fig4 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='drugs', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Drug Crime Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=70)
  fig4.update_geos(fitbounds='locations', visible=False)

  fig4.write_image("DrugCrimeChoropleth.png")
#Showing possession of weapons in each borough 
def figure5():
  fig5 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='possession-of-weapons', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Possession Of Weapons Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=12)
  fig5.update_geos(fitbounds='locations', visible=False)

  fig5.write_image("WeaponPossessionChoropleth.png")

#Showing anti social behaviour in each borough 
def figure6():
  fig6 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='public-order', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Anti-Social Behaviour Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=110)
  fig6.update_geos(fitbounds='locations', visible=False)

  fig6.write_image("ASBOChoropleth.png")

#Showing robbery in each borough 
def figure7():
  fig7 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='robbery', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Robbery Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=55)
  fig7.update_geos(fitbounds='locations', visible=False)

  fig7.write_image("RobberyChoropleth.png")

#Showing shoplifting in each borough 
def figure8():
  fig8 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='shoplifting', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Shop-Lifting Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=120)
  fig8.update_geos(fitbounds='locations', visible=False)

  fig8.write_image("ShopLifingChoropleth.png")
#Showing theft from the person in each borough 
def figure9():
  fig9 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='theft-from-the-person', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Theft From The Person Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=125)
  fig9.update_geos(fitbounds='locations', visible=False)

  fig9.write_image("TheftChoropleth.png")

#Showing vehicle crime in each borough 
def figure10():
  fig10 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='vehicle-crime', 
                      hover_name ='Borough',
                      scope='europe',
                      title="Vehicle Crime Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=300)
  fig10.update_geos(fitbounds='locations', visible=False)

  fig10.write_image("GTAChoropleth.png")
#Showing violent crime in each borough 
def figure11():
  fig11 = px.choropleth(df3,
                      locations='id', 
                      geojson=boundaries, 
                      color='Total Crime', 
                      hover_name ='violent-crime',
                      scope='europe',
                      title="Violent Crime Chloropleth",
                      color_continuous_scale=px.colors.diverging.RdYlGn,
                      color_continuous_midpoint=550)
  fig11.update_geos(fitbounds='locations', visible=False)

  fig11.write_image("ViolenceChoropleth.png")

  #Plot Switches, remove hashtag from function to try out each plot
#------------------------------------------------------------------------------------------------------------------------
#Total Crime Choropleth
#figure1()
#fig1.show()
#Bicycle Theft Choropleth
#figure2()
#fig3.show()
#Drug crime Choropleth
#figure3()
#fig4.show()
#Weapon Possession Choropleth
#figure5()
#fig5.show()
#Anti-Social Behaviour Choropleth
#figure6()
#fig6.show()
#Robbery Choropleth
#figure7()
#fig7.show()
#Shoplifting Choropleth
#figure8()
#fig8.show()
#Theft from the person Choropleth
#figure9()
#fig9.show()
#Vehicle crime Choropleth
#figure10()
#fig10.show()
#Violent crime Choropleth
#figure11()
#fig11.show()