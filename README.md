# Analysis-of-Crime-within-London

A detailed investigation into the distribution of crime and crime sub-categories within London

# Exploring Crime Distribution in London:

## Executive Summary:

The focus of this project was to investigate the distribution of crime across London and more specifically across the 32 inner and outer boroughs of London to see which areas and therefore residents are most likely to experience certain crimes in their area. Our initial framing for this project was to help students like us, navigate an unfamiliar landscape but also for potential investors setting up offices or for families buying properties to be fully aware of the area they are buying into. Especially as property prices continue to rise relentlessly, it is becoming increasingly difficult to judge the quality of the area through property prices alone, so we hope our visualisation can paint the full picture. Crime in London in becoming increasing topical since the rise of knife crime and other violent crime since the beginning of the last decade. We ultimately hope our project can help increase awareness of crime prone areas and thus increase people’s safety.   

For this project we collected 14 categories crime data from all 32 Boroughs using the London Metropolitan Police Crime API for 2021. Our resulting dataset contained just under 74,000 data points which we had to wrangle to make presentable using knowledge of pandas. Our exploratory analysis and visualisations provided both surprising and non-surprising insights we sought to rationalise through further research.
 
## Motivation

As we are both London residents, staying safe is always at the forefront of our minds. Whether that be walking to and from LSE campus late at night or exploring London for the various activities it offers, knowing which areas are more prone to crime and which are relatively safer can offer some peace of mind when planning your trips. Furthermore, property prices in London don’t look like they are slowing down any time soon and thus this project will remain relevant in future years to come since you can collect updated data in the by simply updating the links for the API when the API itself is updated by the Metropolitan police. Another ‘tongue-in-cheek’ motivation for this investigation was as if we were a private investigator or masked vigilante looking to “clean up the streets”. This would provide us with the information as to where to focus our efforts.

This investigation will also allow us to confirm or refute stereotypes of areas in London. London is a very old city, and each 32 Boroughs has built up its own reputation. This investigation will thus allow us to see whether these stereotypes are deserved or if they are now out-dated. 

Moving beyond simply visualising the data, we can use the data we collect to further investigate correlations between other variables and the number of crimes such as:
>- Median Income
>- House Price
>- Years to Purchase a House on median income
>- Population
>- Area

This will push in the direction of drawing some conclusions as to what factors affect the crime rate the most and potentially help us pose some hypotheses as to why the crime is distributed the way it is.


## Data and Methodology:

The first step we had to take in collecting the data for this project was going through the Met Police API documentation and figuring out which parts we had to use to get the results we needed. The first challenge we encountered was that the API was designed for more street-level outcomes rather than large areas. The API has a call limit for areas which contain more than 10,000 crimes. Luckily the areas that we wanted to cover did not exceed this limit since we were only focused on collecting data from the latest month available on the API which was December 2022. Using the API documentation, we realised had to create a polygon around each of the boroughs in London using latitude and longitude coordinates to separate the requests into their respective borough. 

This process was extremely time-consuming as we had to collect these coordinates manually which became the largest challenge at the start of the project. What contributed to the time commitment of this process was that each coordinate had to be formatted in a specific way to fit the documentation of the API and for accuracy, we aimed for at least 15-20 points to capture the best shape of the borough. Once this step was complete and the links were made, the next step was converting the output to a JSON file and inputting the parameters we required, more specifically, the ‘Crime’ and ‘Category’ parameters which resulted in the following data frame. This is an example for Westminster:

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images\Other_Images\EDA_example1.png">
</p>

This wasn’t a very easy form to work with so using our knowledge of pandas and data wrangling we managed to get each Data frame in the following form:
<p align='center'>
    <img src = 'https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Images/EDA_example2.png'>
<p>
We did this for each borough using the respective link we had created and merged the data frames since they all had the same index creating the whole dataset:
<p align='center'>
    <img src ='https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Images/dataset_snapshot.png' width = 800 height = 250>
<p>

> Note: This is just a snapshot of the Data Frame – the real dataset is a lot larger

This provided us with the base to get started on our analysis and visualisations since each row and column can be easily isolated and retrieved individually. 

For aggregate statistics, we simply counted all the responses in the JSON file since this was equal to the number of crimes that it outputted which resulted in a list of total crimes per borough ordered by the order of the list of URLs in the source code. Creating the subsequent data frame was therefore easy and more efficient than manipulating the above dataset.

### Main Challenges

1.	Formatting the coordinates – as aforementioned we had to format the coordinates for the Met Police API but on top of this because we wanted to produce a heatmap which used the Geoplot package which required different formatting of the coordinates. This caused significant delays but was relatively easy to overcome.
2.	Accuracy – as we used a polygon to surround the area of the borough this caused a problem in terms of accuracy since the borough boundaries are not perfect boxes or regular polygons. Taking this into account we tried the best we could under a time constraint and wanted to focus more of our efforts on generating insights and visualisations. 


## Exploratory Data Analysis

Our main data set contains all the crimes divided into each category used by the API as shown above for each Borough. This dataset is relatively easy to read but is difficult to visualise as any viewer would struggle to paint the full picture for each borough and each crime category from just this. As previously mentioned, our data set for just the crime contained just under 74,000 data points for all 33 Boroughs, broken down into 13 categories. 

The values of which ranged from 1 weapon possession in Harrow, to 1173 violent crimes in Greenwich. But to gauge the data from a more “macro” perspective we decided to explore the aggregate data for all 33 boroughs instead of completing plots for the crime categories since we thought the best way to explore this data would be through visualising using a heat map. So, focusing on the aggregate statistics, we created this ordered bar graph to show the number of crimes per borough in one month:

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Plots/Aggregation/agg_plot.png" width = 800 height = 800>
</p>

Alongside this, we wanted concrete summary statistics which we gained using the describe() function in python to get the following summary stats for total crime across each borough:

>- count - 33
>- mean - 2337.515152
>- std - 1006.027433
>- min - 590
>- 25% - 1724
>- 50% - 2120
>- 75% - 3077
>- max - 4326

From this we can see that there is huge variation in. the number of crimes but with the majority in the 1500 to 3000 range. This is likewise demonstrated by the standard deviation of 1006 with values taking a range of 3736. For the other relevant variables broken down by crime category, the distribution will be shown in the heat maps below. And for some key variables, we have made a table.


### Range and distribution of other key variables


| Variable    | Std.dev     | Mean         | Range        |
|-------------|-------------|--------------|--------------|
|Median Income|11,893       |34,051        |70,419        |
|Population   |75,871       |271,576       |386,175       |   
|Crime Rate   |1.06         |1.04          |6.38          |


### Size and shape of our final data set

>- Our final data set has 35 columns (14 pertaining to crime, 14 pertaining to crime rate, 7 pertaining to socioeconomic factors) and 33 Rows (32 Boroughs + City of London)

>- Ignoring Indices and Column titles our data set has 1,155 elements

>- Given the similarity between rows and columns, the dataset's shape is almost square, however as the number of rows does not equal the number of columns, the dataset is rectangular

### Size of individual datasets

>- df2 has 33 rows and 7 columns
>- maindft has 33 rows and 16 columns

> Note: Due to the amount of columns of the dataset, the output was often collapsed.

# Data Analysis

## Background

To give some background we initially conducted research about the different factors that affect crime urban areas. Through our research we found that there are many factors that affect crime all  to varying degrees, including inequality, age demographics, economic issues and proximity to metropolitan areas. We felt as though this analysis would be particularly useful to economists and geographers, alongside civilians who are interested in moving to a safe area. Therefore, we chose to analyse variables such as centricity, population and income factors alongside a few others. We used pandas to transpose the initial dataframe and then merged the csv file with the transposed dataframe using .read_csv and the pandas merge function. This combined dataframe is called "df3".

Some issues to consider are that our data only considers one month, and fluctuations may happen between crime rates depending on the time of year so our analysis may not be wholly reflective. In addition to this, our data was sourced from different data sources and from different times. Incomes and house prices are very dynamic variables so the data that we have sourced for analysis may yield some results that are not wholly relevant today.

## Overview of Plots

### Choropleth Maps

In order to visualise the prevalence of crime in each borough, we decided to use a geographical visualisation called a choropleth map. Doing this meant finding a GEOJson file with the boundaries of the London boroughs. We then created identifiers for each borough which corresponded to their boundary co-ordinates within the GEOJson. To create this we used Plotly’s choropleth function and analysed the data to find a midpoint which would illustrate relatively safe areas (red) vs relatively dangerous areas (green). Below is an example of the heat map for total crime.

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Image/Choropleth/Website_Choros/TotalCrimeChoroFinal.jpg" width = 800 height = 800>
</p>

> Note: An interactive example which displays borough names can be found by locating the output.html file in this repository with location: Images /
Interactive_Map /output.html.

### Issues with choropleth map

We would expect that as the population of a borough increases, ceteris paribus, the crime rate will increase. We therefore realised that we actually need to calculate the rate of each crime adjusting for population. To do this we used pandas to add columns to the dataframe “df3” with the rates of each crime. We then recreated the choropleth maps and got an interesting result.

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Choropleth/Website_Choros/CrimeRateChoro.jpg" width = 800 height = 800>
</p>

### What can we conclude from choropleth maps

As we can see once we adjust for population differences, a completely different picture is painted, the City of London has the highest crime rate, likely due to the low population. We can also see a loose relationship between the centricity of the borough and it’s crime rate. However, this map needs further analysis to analyse this relationship.

### Centricity analysis and issues

To analyse this we created a plot to demonstrate the relationship between the total number of crimes in a borough and the boroughs travel zone.

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Plots/Centricity/crimes_travel_zone_graph.jpeg" width = 800 height = 700>
</p>

As we can see there is actually no clear relationship found on this graph however, one confounding factor could be the relationship between population and centricity. Central areas such as City of London and City of Westminster have lower populations and therefore we would expect them to have a higher crime rate. However, if we were to look to crime rate as opposed to number of crimes, the data would likely tell a different story and this is an area for further exploration.

### Scatter Plots

To visualise the relationships between different crimes and different socioeconomic factors, we merged the dataframe that we created “1.csv” (which contains information on demographics, incomes and house affordability) using Pandas. We used Plotnine to create the scatter graphs and here is an example of one of the graphs that we created. (Other graphs that we created did not show any clear relationship without enumeration of the degree of correlation).

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Scatter_Plots/PlotlyScatterForWebsite.jpg" width = 800 height = 800>
</p>

 As you can see, there is a positive correlation between the two factors. As data scientists though, we wanted to enumerate this information. Initially using numpy to calculate the correlations between variables we realised that this code was unnecessarily bulky and used pandas to create a correlation matrix.

### Correlation Analysis

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Plots/Correlation/InitialCorrelationAnalysis.jpg" width = 800 height = 400>
</p>
 
> Note: This is just a snapshot of the Data Frame – the real dataset is a lot larger

To gain even further insight, we decided to create a correlation matrix heatmap using seaborn, and we discovered that out of the factors listed in the file 1.csv, the only factor that had predictive power over crimes committed was population as can be seen below.

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Plots/Correlation/TotalCrimeCorrelationFinal.jpg" width = 800 height = 800>
</p>

We were surprised by the lack of correlation between income and crime and we pondered why this was the case. We then checked our code for issues and found none. Except for one thing…

Yet again we realised that population is a clear confounding factor, so we remade the correlation matrix using the dataset with crime rates that we made for the choropleth maps and as you can see, the variables in 1.csv have much more predictive power.

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Plots/Correlation/CrimeRateCorrelationFinal.jpg" width = 800 height = 800>
</p>

As we can see median income is now a solid predictor for all crimes except for vehicle crime however the relationship is inversely proportional to what we would expect. We and many others have always been taught to expect that low income would correlate to high crime, however our analysis tells a different story. We hypothesised why and came to the logical conclusion that thieves, burglars and robbers target wealthier areas thus raising crime rates in them. I.e the perpetrators of these crimes aren’t necessarily from the boroughs that they are committed in. Although not possible with current data, it could be interesting to do an analysis on crime committed within a borough by residents of said borough.

Looking at this relationship in the context of our data however, we see that areas such as City of Westminster and City of London are areas with very low populations, which mathematically should contribute to a high crime rate, but also high incomes. This means that these two data points among other unexplored data points could influence the degree of correlation. Removing these extreme data points in the future could allow for a more informative analysis.

> Note: One issue that we found with the correlation matrix was that due to she size of the matrix and number of variables, many of the the correlation calculations are irrelevant and it is difficult to read. And therefore we edited the old matrix to display only the most relevant information.

<p align="center">
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Other_Plots/Correlation/CroppedCRCFinal.jpg" width = 700 height = 600>
</p>

We can also see that population is yet again quite strongly negatively correlated with the different types of crime. However, reasoning would suggest that as population is a key factor in the calculation of crime rates, we sould see a strong relationship between the population of a borough and crime rates within the borough.

# Conclusion

Given the level of interdependence between variables and confounding factors that we may not have considered, it is difficult to isolate the causal mechanisms of crime within London. Although we did see strong positive correlation between median income and crime rate, we believe that this may have been influenced by extreme data points and therefore we wouldn’t suggest that The City of London and other areas with high median income are particularly unsafe to visit. Nor can we suggest that it is safer to visit more deprived areas.

### Suggestions that we can make from the analysis however are:

>- If you wish to take a bike ride, avoid the boroughs Richmond upon Thames and Southwark (217 & 181 instances of bike theft respectively) and instead visit Bexley or Brent (2 instances of bike theft each).

>- If you’re looking to open a shop in London, avoid Richmond upon Thames and Bromley (309 and 301 instances of shoplifting respectively).

>- And if you have aichmophobia avoid Croydon (30 instances of possession of weapons) and instead settle in Harrow (1 instance of possession of weapons).

# Contributions

Website: Jaden Mighten and Tom Baldwin

Managing Github: Jaden Mighten and Tom Baldwin

Initial data collection: Tom Baldwin

Improving data collection code: Jaden Mighten

Gathering Co-ordinates: Jaden Mighten and Tom Baldwin

Cleaning Co-ordinates:Jaden Mighten and Tom Baldwin

Creating API Links: Tom Baldwin

Initial Data Wrangling: Tom Baldwin

Main Data Wrangling:Jaden Mighten

Box-Plots: Tom Baldwin

Bar-Charts:Tom Baldwin

Centricity Analysis:Tom Baldwin

Choropleth Maps: Jaden Mighten

Scatter Graphs: Jaden Mighten

Correlation Analysis: Jaden Mighten

Gathering GEOJSon file: Jaden Mighten

Creating socioeconomic data CSV: Jaden Mighten



