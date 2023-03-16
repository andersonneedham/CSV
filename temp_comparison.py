import matplotlib.pyplot as plt
import pandas as pd

# open csv
dv = pd.read_csv("death_valley_2018_simple.csv")
sw = pd.read_csv("sitka_weather_2018_simple.csv")

# automatic index
dv_tmax = dv.columns.get_loc("TMAX")
dv_tmin = dv.columns.get_loc("TMIN")
sw_tmax = sw.columns.get_loc("TMAX")
sw_tmin = sw.columns.get_loc("TMIN")

# figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# plotting sitka
ax1.plot(sw["DATE"], sw.iloc[:, sw_tmax], c="red")
ax1.plot(sw["DATE"], sw.iloc[:, sw_tmin], c="blue")
ax1.fill_between(
    sw["DATE"], sw.iloc[:, sw_tmax], sw.iloc[:, sw_tmin], facecolor="lightblue"
)
# sw title using index values
ax1.set_title(sw.iloc[0, 1])

# plotting Deat valley
ax2.plot(dv["DATE"], dv.iloc[:, dv_tmax], c="red")
ax2.plot(dv["DATE"], dv.iloc[:, dv_tmin], c="blue")
ax2.fill_between(
    dv["DATE"], dv.iloc[:, dv_tmax], dv.iloc[:, dv_tmin], facecolor="lightblue"
)

# dv title using index values
ax2.set_title(dv.iloc[0, 1])

# x axis
ax1.xaxis.set_major_locator(plt.MaxNLocator(7))
ax2.xaxis.set_major_locator(plt.MaxNLocator(7))

# overall title using the index values
fig.suptitle(
    "Temperature Comparison between " + sw.iloc[0, 1] + " and " + dv.iloc[0, 1]
)

# plot
plt.show()
