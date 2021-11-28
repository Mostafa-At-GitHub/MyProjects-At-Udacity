# <font color=blue>Data Expo 2008 «Airline on-time performance»</font>
## by [<font color=orange>Mostafa Abobakr</font>](https://cutt.ly/MostafaALinkedIn)


## Dataset

> This dataset consisting of __7,009,724 rows__ or data points after removing 4 duplicated points, reports flights in the United States, including carriers, arrival and departure delays, and reasons for delays, during year 2008. I reduced the dataset from 29 to 19 to be 9 columns or features eventually, and I got the carrier names instead of there codes from an other file called _carriers.csv_. I exported the columns to be worked with into 2008_flights.csv after some structuring with SQL for rapid processing this huge data, then I came back again to jupyter notebook to complete the work.

[Download the dataset from here](http://ww2.amstat.org/sections/graphics/datasets/DataExpo2009.zip) (1.6 GB zipped datasets for years from 1987 to 2008)

Features documentation:
- [2009 - Joint Statistical Computing and Statistical Graphics Section](https://community.amstat.org/jointscsg-section/dataexpo/dataexpo2009)
- [United States Department of Transportation - BUREAU OF TRANSPORTATION STATISTICS: Airline On-Time Performance Data](https://web.archive.org/web/20210404234819/https://transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&Yv0x=D)
- [The data. Data expo 09. ASA Statistics Computing and Graphics](https://web.archive.org/web/20191220144712/http://stat-computing.org/dataexpo/2009/the-data.html)
- [United States Department of Transportation - BUREAU OF TRANSPORTATION STATISTICS: Reporting Carrier On-Time Performance (1987-present)](https://web.archive.org/web/20210126184228/https://transtats.bts.gov/Fields.asp?table_id=236)

Supplemental data:
- [Supplemental data. Data expo 09. ASA Statistics Computing and Graphics](https://web.archive.org/web/20191229040110/http://stat-computing.org/dataexpo/2009/supplemental-)
- [airports.csv](https://web.archive.org/web/20191229040110/http://stat-computing.org/dataexpo/2009/airports.csv) for the airports descriptions
- [carriers.csv](https://web.archive.org/web/20191229040110/http://stat-computing.org/dataexpo/2009/carriers.csv) which is listing the carriers codes with names
- [plane-data.csv](https://web.archive.org/web/20191229040110/http://stat-computing.org/dataexpo/2009/plane-data.csv) that holds information about individual planes.

We could use the first two supplemental datasets, but we will not use the last plane-data.csv in our investigation.

You also can use this [Google drive link](https://drive.google.com/drive/folders/1qIX3ZNEzrd4bijppXIjsmn0yksc8q-th) to download the dataset with supplemental data.

Other resources: 
- [Data Expo 2009 - Airline on-time Performance Analysis | by Carlson Hoo | Medium](https://carlson-hoo.medium.com/data-expo-2009-airline-on-time-performance-analysis-bb2e5bcf3042), an individual's previous effort on Medium
- [Airlines Delay | Kaggle](https://www.kaggle.com/giovamata/airlinedelaycauses)

## Summary of Findings

* **1**<sup>**st**</sup>: <u>**related to arrival delays and delay causes in general**</u>⮚
    <br>➷ 'Carrier' as well 'Weather' were the most common to cancel a flight. 
    <br>➷ Flights-cancellation due 'Security' doesn't seem to be the common.
    <br>➷ Most arrival delays were of 15 minutes to about 78 minutes.
    <br>➷ More higher frequencies were for "Carrier" and "National Air System" lower-delays values than other delay-causes delays.
    <br>➷ 'Carrier' delays exceeded with the highest spread and outliers.
    <br>➷ 'NAS' delays had more lower-values frequencies.
    <br>➷ In general, Weather-delays had the highest mean, median, the wider IQR, and a wider range from its higher median to its third quartile over other-causes delays. 
    <br>➷ Flights that had weather-delays were probably to have the most arrival delays in general.
    <br>➷ Arrival delays due to 'Weather' had a higher mean, median (which is about 62 minutes), with a larger third quartile range, and a more wider greater values distribution from about 55 minutes to about 225 minutes than arrival delays due to other causes.
    <br>➷ Much more frequencies for arrival delays due to 'NAS'.
    <br>➷ For the whole flights of 15+ min. arrival delay, in general, arrival-delays due to 'Security' had the lowest median, ranges, as well outliers.
    <br>➷ For all delayed or flights of 15+ arrival delay, there were some kind of linearity between arrival delays and delays of different delay-causes, at some point before 250 minutes of causes-delays (and about 50 minutes for sampled data). 
    <br>➷ In general, arrival delays had more stronger moderate correlation with carrier-delays.
    <br>➷ 'Carrier' and 'NAS'-delays had more higher correlation than 'Weather'-delays with arrival delays.
<br>
    
* **2**<sup>**nd**</sup>: <u>**related to 'Months'**</u>⮚
    <br>➷ All 2008 months had close-ratios of recorded total flights frequencies.
    <br>➷ Months 'Feb', 'Dec', 'Jan', and 'Mar', had the highest flights-cancellation counts.
    <br>➷ 'May', 'Nov', and 'Oct' had the lowest flights-cancellation counts.
    <br>➷ 'Feb' exceeded in the ratio of cancelled flights, then 'Dec' and 'Jan',  which are notable to be of 'Winter' season.
    <br>➷ "Weather" had the highest impact to cancel flights within months 'Feb', 'Dec', 'Jan', 'Mar', as well 'Sep', almost for half of the year.
    <br>➷ Months 'Dec', 'Jun', 'Feb', and 'Mar' had the highest arrival delays means.
    <br>➷ 'Sep' and 'Nov' had the lowest arrival delays means.
    <br>➷ 'Weather' had the highest impact on flights arrival delays within different 2008 months.
<br>
    
* **3**<sup>**rd**</sup> <u>**related to 'Carriers'**</u>⮚
    <br>➷ 'Southwest Airlines Co.' recorded the highest total flights count within 2008; more than twice of carrier's in next order.
    <br>➷ Carriers 'American Eagle Airlines Inc.', 'American Airlines Inc.', 'Skywest Airlines Inc.', 'Southwest Airlines Co.', 'United Air Lines Inc.', and 'Expressjet Airlines Inc.', had the highest flights-cancellation counts.
    <br>➷ 'Hawaiian Airlines Inc.', 'Frontier Airlines Inc.', and 'Aloha Airlines Inc.' had the lowest flights-cancellation counts.
    <br>➷ "Carrier" procedures had the highest impact to cancel flights within 11 Airlines carriers of 20.
    <br>➷ "Weather" had the highest impact to cancel flights within 9 Airlines carriers of 20.
    <br>➷ "NAS" or National Air System had the second highest impact to cancel flights within 5 Airlines carriers of 20.
    <br>➷ 'American Airlines Inc.'  had more cancellations due to 'Carrier'.
    <br>➷ 'Hawaiian Airlines Inc.'s flights-cancellation were because of 'Carrier', as a majority.
    <br>➷ 'Aloha Airlines Inc.'s 42 cancelled-flights were because of 'Carrier'.
    <br>➷ Carriers 'American Airlines Inc.', 'Mesa Airlines Inc.', 'Comair Inc.', 'United Air Lines Inc.', 'JetBlue Airways', and 'Continental Air Lines Inc.', had the highest arrival delays means.
    <br>➷ 'Pinnacle Airlines Inc.', 'US Airways Inc.', and 'Hawaiian Airlines Inc.', had the lowest arrival delays means.
    <br>➷ Arrival delays mean of 'Aloha Airlines Inc.' was about negative 3 minutes, indicating almost no arrival delays.
    <br>➷ On average, 'Weather' had the highest impact on flights arrival delays within almost all carriers, notably in 'JetBlue Airways', except in case of 'Frontier Airlines Inc.'
    <br>➷ Arrival delays due to 'Security' may had greater medians and more greater-values distributions, like in 'United Air Lines Inc.', 'Delta Air Lines Inc.' and 'Aloha Airlines Inc.'.

#### Interpretations and conclusions not included in Explanatory presentation, from Exploratory analysis⮚

- 'Carrier' and 'NAS' had the largest counts of lower-values delays for different months, though 'NAS' exceeded in this almost all months. Some months had much more lower causes-delays values than others.

- 'Weather'-delays had the highest medians, and the largest third quartile ranges all over months. Then came 'Carrier'-delays, except about 3 or 4 months where 'NAS'-delays had larger medians, but smaller third quartile ranges also. At last 'Security'-delays had lowest medians and third quartile ranges across months.

- 'Weather'-delays were the highest on average within different 2008 months, notably in 'Jul' and 'Sep'. Then 'Carrier'-delays, 'NAS' or national air system-delays, and 'Security'-delays at last, come in order respectively.

- Greater-values distributions due to 'Weather'-delays were the largest all over months.

- 'Carrier', as well 'NAS'-delays, had the largest counts of lower-values for different carriers, especially in cases of 'Southwest Airlines Co.' and 'American Airlines Inc.'. Some carriers had much more lower causes-delays values than others.

- There weren't any 'Security'-delays in 'AirTran Airways Corporation'. Unlike in 'Frontier Airlines Inc.', where the highest median, as well the largest second and third quartiles ranges, were for 'Security'-delays against other delay-causes, in the carrier. 'Security'-delays in the same carrier had the largest IQR range, as well the range from the second to the third quartiles.

- Weather-delays distributions were the highest at all within 'Mesa Airlines Inc.', 'Expressjet Airlines Inc.', 'JetBlue Airways', 'Skywest Airlines Inc.', 'AirTran Airways Corporation', and 'Aloha Airlines Inc.'.

- 'Weather'-delays were the highest on average within almost the majority of carriers. Then also, in general, 'Carrier'-delays, 'NAS' or national air system-delays, and 'Security'-delays at last, came in order, except in few carriers. Unlike the rule, 'Security'-delays were the highest on average within 'Frontier Airlines Inc.' and 'Delta Air Lines Inc.'. 'Security'-delays also may were the second or the third in other carriers, such as 'United Air Lines Inc.' and 'American Airlines Inc.'. However, 'AirTran Airways Corporation' flights doesn't seem to be delayed due to security at all.

- Unlike usual regarding different-causes delays within all carriers, 'Northwest Airlines Inc.' had the highest outliers of 'Carrier'-delays, that almost could reach about 2500 minutes delay.

## Key Insights for Presentation

I used the dataset to gain insights that could help make improvements against the flights delaying's, or to make backed findings about the best carriers with less delaying's.

> After finishing some work of columns-structuring using SQL, I extracted the columns I thought as helpful for this investigation, they were _['Month', 'Carrier', 'ArrDelay', 'Cancelled','CancellationCode','CarrierDelay','WeatherDelay','NASDelay','SecurityDelay']_ into __'df_inv'__ dataframe.

> __From 'df_inv', I derived:__<br>
__1__ _**'airline_cancelled'**_ dataframe for data points of cancelled flights data<br>
__2__ _**'on_time'**_ dataframe for flights with less than 15 min. arrival delay and not null, or data points with arrival delays less than 15 minutes and not null<br>
__3__ _**'df_inv_15'**_ for flights with arrival delays that equal 15 minutes or more, then i **sampled 'df_inv_15_samp'** from them. I melted the delay-causes columns within 'Cause' column, and I put their values in 'Minutes' column. Next, I removed 'Minutes' with zero, less or null values, _**producing 'melt_15' and 'melt_samp_15'**_ dataframes _for using new created columns from melting in investigating relationships among delay-causes and other features like month, carrier, and arrival delay._