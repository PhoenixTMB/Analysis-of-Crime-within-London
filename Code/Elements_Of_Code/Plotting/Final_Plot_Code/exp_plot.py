import numpy
import pandas as pd
from plotnine import *

df = pd.read_csv('travelzone_df.csv')
df2 = df.drop('index', axis=1)
df_main = df2.drop('Unnamed: 0', axis=1)

print(df_main.dtypes)

borough = df_main['Borough'].to_list()

borough.append('Greenwich')

crimes = df_main['Number of Crimes'].to_list()

crimes.append(3195)

df_new = pd.DataFrame({'Borough_':borough, 'Number of Crimes_':crimes})
print (df_new)

borough_count = df_new[['Borough_', 'Number of Crimes_']].sort_values(by='Number of Crimes_', ascending = True)
borough_count['Borough_'] = pd.Categorical(borough_count['Borough_'], categories=borough_count['Borough_'].tolist())

print(borough_count)

p = (ggplot(borough_count, aes(x='Borough_', y = 'Number of Crimes_'))
    +geom_col()
    +coord_flip()
    +labs(title = 'Crimes per London Borough December 2022', x= 'Borough', y='Number of Crimes'))
p.save(filename = 'agg_plot.png', height=15, width=15, dpi=1000)

p2 = (
    ggplot(df_new, aes(y='Number of Crimes_',x=0))
    + geom_boxplot(colour="rebeccapurple", fill="lightskyblue")
    
)
p2.save(filename = 'agg_boxplot.png', height=15, width=15, dpi=300)
