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
    <img src="https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/first_dframe.png">
</p>

This wasn’t a very easy form to work with so using our knowledge of pandas and data wrangling we managed to get each Data frame in the following form:
<p align='center'>
    <img src = 'https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Picture%202.png'>
<p>
We did this for each borough using the respective link we had created and merged the data frames since they all had the same index creating the whole dataset:
<p align='center'>
    <img src ='https://github.com/PhoenixTMB/Analysis-of-Crime-within-London/blob/main/Images/Picture%303.png'>
<p>
> (Note: This is just a snapshot of the Data Frame – the real dataset is a lot larger)
