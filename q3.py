"""
The total amount for the electricity bills for a house for an entire standard year (assuming
365 days in the year) are $1368 to the nearest dollar. If the tariff had a supply charge of
107.7685 cents per day, and an electricity charge of 30.0605 cents per unit (flat rate), then
assuming the average power was the same throughout the year, what would be the average
daily energy use given on the electricity bill? What would the daily energy use be in joules?
What would be the average power used by the house during a typical day? [5 marks]
"""

# Let's break the question down into components
# 1. Determine average daily energy use
# 2. Calculate daily energy use in joules (should be a simple calculation)
# 3. Calculate typical average daily power use

# And some steps to get there
# 

# Let's configure some variables from the question above
total_annual_bill = 1368  # Our total annual bill, in dollars
daily_supply_cpd = 107.7685  # Daily supply charge, in cents per day
electricity_cost_cpu = 30.0605 # Electricity cost, in cents per unit
days_in_year = 365

# Step 1. Let's calculate our annual supply charge
# Total = daily * days in year
annual_total_supply_cents = daily_supply_cpd * days_in_year

# Turns the number into an float rounded to two decimal places
annual_total_supply_cents = float(round(annual_total_supply_cents, 2))

# And convert to dollars
annual_total_supply_dollars = annual_total_supply_cents / 100

# And round to two decimal places
annual_total_supply_dollars = float(round(annual_total_supply_dollars, 2))

# Step 2. We now need to calculate the total annual electricity consumption cost, which is our total annual bill minus the annual supply charge
# The annual supply charge is a fixed cost, so we can subtract it from our total annual bill to get our total annual electricity consumption cost
annual_total_consumption_dollars = total_annual_bill - annual_total_supply_dollars

# And rounded, again
annual_total_consumption_dollars = float(round(annual_total_consumption_dollars, 2))

# Step 3. We need to cetermine our average daily electricity consumption in units
# We can do this by dividing our total annual electricity consumption cost by the cost per unit, and then dividing by the number of days in a year
# We need to convert dollars to cents for this calculation
average_daily_electricity_consumption_kwh = ((annual_total_consumption_dollars * 100) / electricity_cost_cpu) / days_in_year

# And round to two decimal places
average_daily_electricity_consumption_kwh = float(round(average_daily_electricity_consumption_kwh, 2))

# Step 4. We need to convert kWh to joules.
# 1 kWh = 3.6 x 10^6 Joules
joules_per_unit = 3.6e6  # Python notation for 3.6 x 10^6

# So it's a simple multiplication to get our daily energy use in joules
daily_energy_use_joules = average_daily_electricity_consumption_kwh * joules_per_unit

# Step 5. We can now calculate the average power used by the house during a typical day
# 1 watt = 1 joule per second
seconds_per_day = 86400  # Number of seconds in a day: 60 * 60 * 24

# Average power is energy used divided by time
average_power_watts = daily_energy_use_joules / seconds_per_day

print(f"annual_total_supply_dollars: {annual_total_supply_dollars}")
print(f"annual_total_consumption_dollars: {annual_total_consumption_dollars}")
print(f"average_daily_electricity_consumption_kwh: {average_daily_electricity_consumption_kwh}")
print(f"daily_energy_use_joules: {daily_energy_use_joules}")
print(f"average_power_watts: {average_power_watts}")
