import matplotlib.pyplot as plt
from main_data_collection import urls, names

#use the len response to count the the number of crimes which we realised was easier than Pandas concat 
agg_crimes = []
for url in urls:
  resp = requests.get(url)
  crime_tot = int(len(resp.json()))
  agg_crimes.append(crime_tot)

#summary statistics - only useful summarry stats was for total crimes per borough
s = pd.Series(agg_crimes)
stats = s.describe()

#used underground website to find the travel zones of each borough in the right order
zones = [1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 3, 4, 2.5, 5, 2.5, 6, 6, 4, 4, 5, 3, 5, 3, 6, 6, 4, 3, 4, 4, 5, 3]
agg_df_with_zones = pd.DataFrame({'Borough': names, 'Number of Crimes':agg_crimes, 'Travel Zone':zones})
#ordered the boroughs in the crimes - this was feedback from the last presentation
df_sorted = agg_df_with_zones.sort_values(by=['Number of Crimes'])

col1 = 'cornflowerblue'
col2 = 'lightcoral'

#this is the plot - used matplotlib to make it 'pretty'
fig,ax = plt.subplots()

ax.bar(df_sorted['Borough'],
        df_sorted['Number of Crimes'],
        color=col1, 
        )

ax.set_xlabel("Borough", fontsize = 22)
ax.set_xticklabels(df_sorted['Borough'], rotation = 45, ha = 'right', fontsize = 12)
ax.set_ylabel("Number of Crimes",
              color='blue',
              fontsize=22)

ax2=ax.twinx()

ax2.plot(df_sorted['Borough'], df_sorted["Travel Zone"],color='red',marker="o", linewidth = 3)
ax2.set_ylabel("Travel Zone",color='red',fontsize=22)

plt.title('Number of Crimes per Borough compared with Borough Centricity', fontsize = 25)
fig.set_figheight(10)
fig.set_figwidth(25)

fig.show()
fig.savefig('crimes_travel_zone_graph.jpeg', dpi = 300, bbox_inches='tight')