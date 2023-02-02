import plotnine
from plotnine import *
plot1 = ggplot(df3, aes(x='Median Income',y='Total crime')) + geom_point() + labs(title = "Median Income vs Total Crime")
plot1.save("Median Income vs Total Crime", dpi=600)
plot2 = ggplot(df3, aes(x='Population density',y='Total crime')) + geom_point() + labs(title = "Population vs Total Crime")
plot2.save("Population Density vs Total Crime", dpi=600)
plot3 = ggplot(df3, aes(x='Years to Purchase a House on Median Income',y='Total crime')) + geom_point() + labs(title = "Years to Purchase a House on Median Income vs Total Crime")
plot3.save("House affordability vs Total Crime", dpi=600)
plot4 = ggplot(df3, aes(x='Population',y='Crime Rate')) + geom_point() + labs(title = "Population vs Crime rate")
plot4.save("Population vs Crime rate", dpi=600)
plot5 = ggplot(df3, aes(x='Median Income',y='Crime Rate')) + geom_point() + labs(title = "Median Income vs Crime rate")
plot5.save("Median Income vs Crime rate", dpi=600)