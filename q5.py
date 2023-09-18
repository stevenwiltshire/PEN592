"""
A 45 kW rated solar power system has its power output and the Solar irradiance on the PV
system measured every hour during daylight hours over a day starting at 5am. Based on the
following data, create a scatter plot of the power output of the PV system against the solar
irradiance and comment on the relationship between the two. Based on the data, what
information can you deduce about this day? (Assuming that a clear day in summer will have
a maximum irradiance reaching the ground of 1kW/m2) [5 marks]
Time of day Solar Irradiance on the PV
system (kW/m2)
Power output from the PV
system (kW)
Time    
05:00   0.149   5.986
06:00   0.324   12.674
07:00   0.482   18.342
08:00   0.597   22.138
09:00   0.662   24.132
10:00   0.686   24.787
11:00   0.677   24.454
12:00   0.631   22.983
13:00   0.54    20.158
14:00   0.397   15.12
15:00   0.229   8.993
16:00   0.077   3.099
17:00   0.002   0.081
18:00   0   0
"""

import pandas as pd
import matplotlib.pyplot as plt

# Let's create a dataframe from the data above. We'll put everything in a dictionary and then use the keys as the headers for our dataframe.
# Times need to be strings, because they're not numbers. Other values can be floats. I probably don't need a dataframe, but... why not?
data = {
    'time': ['05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00'],
    'solar_irradiance': [0.149, 0.324, 0.482, 0.597, 0.662, 0.686, 0.677, 0.631, 0.54, 0.397, 0.229, 0.077, 0.002, 0],
    'power_output': [5.986, 12.674, 18.342, 22.138, 24.132, 24.787, 24.454, 22.983, 20.158, 15.12, 8.993, 3.099, 0.081, 0]
}

# And create a dataframe from the dictionary
datadf = pd.DataFrame(data)

# We'll use matplotlib to create a scatter plot
plt.figure(figsize=(12, 6))  # Set the size of the plot
plt.scatter(datadf['solar_irradiance'], datadf['power_output'], c='orange')  # We have been asked to create a scatter plot, so I will. Let's go with orange, because blue is boring and orange is kind of like the sun.
plt.title('Power Output of PV System vs. Solar Irradiance')  # Sets the title of our graph
plt.xlabel('Solar Irradiance (kW/m2)')  # Sets the x axis label
plt.ylabel('Power Output (kW)')  # And the y axis label

# Generate the graph
plt.grid(True)  # We want a grid
plt.legend()  # We also want a legend
plt.show()  # This will generate a popup in VS Code with the graph. Save and close to move on.

# OK - so that has generated a graph of the power output versus the solar irradiance, but let's make one showing power output versus time of day.
# I think we'll use a vertically oriented bar chart for this one.
plt.figure(figsize=(12, 6))  # Set the size of the plot
plt.bar(datadf['time'], datadf['power_output'], color='orange')  # I think we want a bar chart
plt.xlabel('Time of Day')  # Sets the x axis label
plt.ylabel('Power Output (kW)')  # And the y axis
plt.title('Power Output of PV System vs. Time of Day')  # Sets the title of our graph

plt.grid(True)  # We want a grid
plt.legend()  # We also want a legend
plt.show()  # This will generate a popup in VS Code with the graph. Save and close to move on.


# Let's now make a graph of the time of day versus solar irradiance
plt.figure(figsize=(12, 6))  # Set the size of the plot
plt.bar(datadf['time'], datadf['solar_irradiance'], color='orange')  # Let's use an orange bar chart again
plt.xlabel('Time of Day')  # Sets the x axis label
plt.ylabel('Solar Irradiance (kW/m2)')  # And the y axis
plt.title('Solar Irradiance vs. Time of Day')  # Sets the title of our graph

plt.grid(True)  # We want a grid
plt.legend()  # We also want a legend
plt.show()  # This will generate a popup in VS Code with the graph. Save and close to move on.

