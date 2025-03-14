

library(tidyverse)

setwd("C:/Users/Growell/QC-tips-and-tricks")
getwd()
	
df <- read_csv("BirdObservationsThru2022_3.csv")
df
	
head(df)
tail(df)
	
view(df)
	
glimpse(df)

# Here, I am selecting a small subset of data to get started...

df |> select(Make, Model, Model_Year)
	
	