
# -----------------------
# QCing monitoring data
# R tidyverse version
# Gareth Rowell 2/14/2025
# -----------------------


library(tidyverse)
library(lubridate)

# Step 1 - loading the data

setwd("C:/Users/Growell/QC-tips-and-tricks")
getwd()
	
df <- read_csv("BirdObservationsThru2022_3.csv")

glimpse(df)
	

# Step 2 - selecting data 

df |> select(ParkUnit, EventDateTime, Temperature_C,  Rain, CommonName, Distance) |> view()


# Step 3 - create unique lists for text data

df |> distinct(ParkUnit) 

df |> distinct(CommonName) |> 
   arrange(CommonName) |>
   print(n = 223) 
   

# Step 4 - create group by counts for categorical data

df |> group_by(Rain) |> count() 


# Step 5 - create bar charts for dates and numerical columns

df2 <- df |> select(EventDateTime, Temperature_C, Distance) |>
	filter(Temperature_C > -9999) |>
	filter(Distance > -9999) |>
    mutate(
	obs_date = as.Date(EventDateTime),
	obs_time = hms::as_hms(EventDateTime)
	)
	
ggplot(df2, aes(x = obs_date)) +
    geom_histogram()
	
ggplot(df2, aes(x = obs_time)) +
    geom_histogram()	
	
ggplot(df2, aes(x = Temperature_C)) +
    geom_histogram()

ggplot(df2, aes(x = Distance)) +
    geom_histogram()












	
	