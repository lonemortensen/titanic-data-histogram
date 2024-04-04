# =======================================================================
# Project: Titanic Dataset
# Description: Selecting and summarizing data and determining probability.
# The project uses Python's NumPy and Matplotlib libraries to first select and organize data for comparison and examination, and then create histograms to visually compare the data. The result is a comparison of Titanic fare prices and passenger survival rates.
# Background: Coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

# ==== *** ====

# The main.py file contains code that:
# - accesses data from the dataset and converts the data to a NumPy array.
# - uses NumPy arrays to slice data from the dataset and convert the arrays
# from two-dimensional to one-dimensional arrays to make the code easier to
# work with.
# - pulls and organizes data into separate lists for comparison of data.
# - summarizes data for examination.
# - uses Matplotlib to create histograms for data comparison.
# =======================================================================

import csv
import numpy as np
import matplotlib.pyplot as plt

# Accesses and retrieves csv data as py list, views headers to get column index numbers, and converts data list to NumPy array:
with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  # Gets headers from first row:
  headers = next(data)
  # Retrieves all rows as a py list:
  data = list(data)
  # Converts data into NymPy array:
  data = np.array(data)

# Slices data from the "Survived" column (index 0) and converts to 1D array:
survived = np.array(data[:, [0]], dtype=int).flatten()

# Slice data from the "Fare" column (index 7) and converts to 1D array:
fare = np.array(data[:, [7]], dtype=float).flatten()

# Holds data from the for loop:
fare_survived = []
fare_not_survived = []

# Tests if data in each index in "Survived" column is equal to 1 ("survived") and adds the data from the equivalent index in the "fare" array to the appropriate empty list:
for index in range(0, len(fare)):
  if survived[index] == 1:
    fare_survived.append(fare[index])
  else:
    fare_not_survived.append(fare[index])

### Summarizes lists for examination:

# Summarizing each list to find the average fare:
print(
  f"The average fare of those who survived was: ${round(np.mean(fare_survived), 2)}"
)
print(
  f"The average fare of those who did not survive was: ${round(np.mean(fare_not_survived), 2)}"
)

# Summarizing each list to find the median fare:
print(
  f"The median fare of those who survived was: ${round(np.median(fare_survived), 2)}"
)
print(
  f"The median fare of those who did not survive was: ${round(np.median(fare_not_survived), 2)}"
)

### Creates histograms containing data for those who survived vs those who did not survive:

# Creates 15 bins for fares, starting at $0 and ending at $240 (max ticket price):
bins = range(0, 240, 15)

plt.hist(fare_not_survived, bins, histtype="bar", color="red", alpha=0.5)
plt.hist(fare_survived, bins, histtype="bar", color="blue", alpha=0.5)

plt.xlabel("Fare Price")
plt.ylabel("Number of Passengers")
plt.title("Titanic Fare Prices and Passenger Survival Rates")

# Adds a legend to histogram:
# - gca() = get the current axes
# - legend() = places a legend on the axis
plt.gca().legend(("Did Not Survive", "Survived"))

plt.xticks(range(0, 240, 20))
# Y-axis ticks do not exceed 360 as number of passengers who died in each range did not exceed 360:
plt.yticks(range(0, 360, 25))

plt.savefig("comparing_titanic_fares")
