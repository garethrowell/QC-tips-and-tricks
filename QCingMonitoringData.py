

# -----------------------
# QCing monitoring data
# Python pandas version
# Gareth Rowell 3/14/2025
# -----------------------


import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)


# Step 1 - loading the data (I'm starting my IPython session 
# in the project directory)

	
df = pd.read_csv("BirdObservationsThru2022_3.csv")
df

# Step 2 - selecting data that we will be QC'ing

df[["ParkUnit", "EventDateTime", "Temperature_C",  "Rain", "CommonName", "Distance"]]

# Step 3 - create unique lists for text data

sorted(df["ParkUnit"].unique())

sorted(df["CommonName"].unique())


# Step 4 - create group by counts for categorical data

df.groupby("Rain").size()


# Step 5 - create bar charts for dates and numerical columns

# Dates are complicated by type conversion and explicitly generating counts 

df["EventDateTime"] = pd.to_datetime(df["EventDateTime"], errors='coerce')

df["EventDate"] = df["EventDateTime"].dt.date
df["EventHour"] = df["EventDateTime"].dt.hour 

# Create counts manually

date_counts = df["EventDate"].value_counts().sort_index()
time_counts = df["EventHour"].value_counts().sort_index()

plt.bar(date_counts.index, date_counts.values, color="skyblue", edgecolor="black")
plt.xlabel("Date")
plt.ylabel("Frequency")
plt.show()

plt.bar(time_counts.index, time_counts.values, color="skyblue", edgecolor="black")
plt.xlabel("Hour of the Day")
plt.ylabel("Frequency")
plt.show()


# Numericals ---------------------------

# Filter rows where Temp_C > -9999
filtered_df = df[df["Temperature_C"] > -9999]

# Plot a histogram of the filtered Temperature_C column
plt.hist(filtered_df["Temperature_C"], bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram of Filtered Temperature (°C)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()


# Filter rows where Distance > -9999
filtered_df = df[df["Distance"] > -9999]

# Plot a histogram of the filtered Temperature_C column
plt.hist(filtered_df["Distance"], bins=100, color="skyblue", edgecolor="black")
plt.title("Histogram of Filtered Distance (°C)")
plt.xlabel("Distance (m)")
plt.ylabel("Frequency")
plt.show()






