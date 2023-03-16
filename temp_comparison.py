import matplotlib.pyplot as plt
import pandas as pd

# read in csv files
dv = pd.read_csv("death_valley_2018_simple.csv")
sw = pd.read_csv("sitka_weather_2018_simple.csv")

# get the index values for TMAX and TMIN
dv_tmax = dv.columns.get_loc("TMAX")
dv_tmin = dv.columns.get_loc("TMIN")
sw_tmax = sw.columns.get_loc("TMAX")
sw_tmin = sw.columns.get_loc("TMIN")

# set up the figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# plot the Sitka data
ax1.plot(sw["DATE"], sw.iloc[:, sw_tmax], c="red")
ax1.plot(sw["DATE"], sw.iloc[:, sw_tmin], c="blue")
ax1.fill_between(
    sw["DATE"], sw.iloc[:, sw_tmax], sw.iloc[:, sw_tmin], facecolor="lightblue"
)
ax1.set_title("SITKA AIRPORT, AK US")

# plot the Death Valley data
ax2.plot(dv["DATE"], dv.iloc[:, dv_tmax], c="red")
ax2.plot(dv["DATE"], dv.iloc[:, dv_tmin], c="blue")
ax2.fill_between(
    dv["DATE"], dv.iloc[:, dv_tmax], dv.iloc[:, dv_tmin], facecolor="lightblue"
)
ax2.set_title("DEATH VALLEY, CA US")

# Format x-axis
ax1.xaxis.set_major_locator(plt.MaxNLocator(7))
ax2.xaxis.set_major_locator(plt.MaxNLocator(7))

# set the overall title
fig.suptitle(
    "Temperature Comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
)

# show the plot
plt.show()
