"""
For the country of Israel, use the IEA world energy balances highlights excel file (see the
resources area for topic 2) to examine and compare the final energy consumption by fuel
type for two sample years, 1995 and 2015, and total final energy consumption by use sector
for the same sample years. Use appropriate graphs to illustrate this information and discuss
the meaning of the results. For the same country include a graph showing how the
contribution of renewable energy sources and fossil fuel sources to its electricity supply in
GWh has changed with time (for all the years that there is data in the file) and comment on
these changes and what you think they mean for that country. [10 marks]

Israel:
    - Final energy consumption by fuel type for 1995 and 2015
        - Stacked area
    - Final energy consumption by use sector for 1995 and 2015
        - Stacked area
    - 
    
    - Graph to show contribution of renewable energy sources and fossil fuel sources to its electricity supply in GWh over time (all years)
        - Stacked area chart
        
Step 1: I'm not entirely sure how to use Python to interact with Excel pivot tables, so I'm going to export the data from the pivot tables to CSV files and then read those into Python.
    - I'm only going to export the data for Israel, and I'm going to drop the country from the CSV file, because I don't need it.
    - We can index by fuel type.

Step 2: We load the data into dataframes using Pandas
    
"""

import pandas as pd  # Pandas is probably going to be most useful here
import matplotlib.pyplot as plt  # And we'll use matplotlib for our graphs

# Loads our final consumption by fuel type CSV
total_final_consumption_fueltype_df = pd.read_csv("israel-tfc.csv")  # Read the data from the CSV file into a dataframe
total_final_consumption_fueltype_df = total_final_consumption_fueltype_df.set_index("Product")  # Set the index to the fuel type
# We need to drop the total row, because we don't need it
total_final_consumption_fueltype_df = total_final_consumption_fueltype_df.drop("Total", axis=0)  # Drop the total row

# And our consumption by sector CSV
total_final_consumption_bysector_df = pd.read_csv("israel-TFCbysectortotal.csv")

# And our total output CSV
total_output_df = pd.read_csv("israel-ffrs.csv")
total_output_df = total_output_df.set_index("Product")  # Set the index to the fuel type
# We can drop the "Flow" column
total_output_df = total_output_df.drop("Flow", axis=1)

# We need only 1995 and 2015
tfcft_years = total_final_consumption_fueltype_df[["1995", "2015"]]

# We want to calculate the percentage of each fuel type for each year
tfcft_pct = tfcft_years.div(tfcft_years.sum()) * 100


# Let's define a colour scheme - but we'll call it "color_scheme" because the library is American
color_scheme = [
    '#1f77b4',  # Blue
    '#ff7f0e',  # Orange
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#9467bd',  # Purple
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#7f7f7f'   # Gray
]

fig, ax = plt.subplots(figsize=(12, 6))  # Set the size of the plot

bottoms = [0, 0]  # We need to set the bottom of the graph to zero

print(tfcft_pct)


# Now we need to loop over the list of fuel products and make a bar for each one...
for index, row in tfcft_pct.iterrows():
    label = index
    color = color_scheme
    ax.bar(row.index, row.values, bottom=bottoms, label=index)
    bottoms = [bottoms[i] + row.values[i] for i in range(len(row))]  # We need to update the bottom of the graph for the next iteration

ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
ax.set_title('Israel, Product Use by Percentage for Years 1995 and 2015')
ax.legend()
plt.show()

# Let's also print the dataframe...
print(tfcft_pct)

# And save it as an Excel file so I can paste it more easily into Word
tfcft_pct.to_excel("total_consumption_type_pct.xlsx")

# OK - let's get to work on the by sector stuff...
# Create figure and axis objects and maintain the same size as above
fig, ax = plt.subplots(figsize=(12, 6))

# Now we need to loop over the list of fuel products and make a bar for each one...
# I'm going to try a different approach that allows me to select a colour from the colour scheme
bottoms = {'1995': 0, '2015': 0}  # Set the bottoms again

for index, row in total_final_consumption_bysector_df.iterrows():
    label = row['Flow']
    color = color_scheme[index % len(color_scheme)]  
    ax.bar('1995', row['1995'], bottom=bottoms['1995'], label=label, color=color)
    bottoms['1995'] += row['1995']
    ax.bar('2015', row['2015'], bottom=bottoms['2015'], color=color)
    bottoms['2015'] += row['2015']

# Add title and labels
ax.set_xlabel('Year')
ax.set_ylabel('Total Energy Use (PJ)')
ax.set_title('Total Energy Flows in 1995 and 2015')
ax.legend(title="Flow")
plt.show()


# Let's also print the dataframe, but only the 1995 and 2015 columns
print(total_final_consumption_bysector_df[['Flow', '1995', '2015']])

# And save it, once again
total_final_consumption_bysector_df.to_excel("total_consumption_sector.xlsx")

# Let's create a stacked area graph to show fossil fuel versus renewable energy sources for electricity supply in GWh over time

# We need to transpose the dataframe so that the years are the index
total_output_df = total_output_df.transpose()


# Let's change the aspect ratio because it's a wide set of data
plt.figure(figsize=(16, 8))  # 2:1

plt.stackplot(total_output_df.index, total_output_df['Fossil fuels'], total_output_df['Renewable sources'], 
              labels=['Fossil fuels', 'Renewable sources'], alpha=0.6)  # Alpha is the transparency of the graph

plt.xticks(total_output_df.index[::5], rotation=45)  # We want to show every fifth year, and rotate the labels 45 degrees, for clarity

plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)  # And a grid will help us see the data more clearly


# Let's set up some labels and titles and put a legend in some blank space
plt.title('Stacked Area Chart of Electricity Output from Fossil Fuels and Renewable Sources (1971-2020)')
plt.xlabel('Year')
plt.ylabel('Electricity output (GWh)')
plt.legend(loc='upper left')

plt.show()