
from gplearn.genetic import SymbolicRegressor
from sklearn.utils.random import check_random_state

# OK - let's try to figure out the relationship between power output and solar irradiance.
# I haven't used symbolic regression techniques much, so I'm going to use the gplearn library to do this - and some help from GitHub Copilot populate the parameters.

X = datadf['solar_irradiance'].values.reshape(-1, 1)  # We turn the solar irradiance values into a numpy array, and reshape it to be a single column
y = datadf['power_output'].values  # And the power output values into a numpy array

# We need a random state for this, so let's create one
random_state = check_random_state(0)

# And let's create a symbolic regressor
est_gp = SymbolicRegressor(population_size=5000,
                            generations=20,
                            stopping_criteria=0.01,
                            p_crossover=0.7,
                            p_subtree_mutation=0.1,
                            p_hoist_mutation=0.05,
                            p_point_mutation=0.1,
                            max_samples=0.9,
                            verbose=1,
                            parsimony_coefficient=0.01,
                            random_state=random_state)

# Now we try to fit the model
est_gp.fit(X, y)

print(f"Symbolic equation: {est_gp._program}")


# Plotting the original data and the curve obtained from symbolic regression
plt.figure(figsize=(12, 8))
plt.scatter(X, y, s=20, c='blue', label='Data points')
plt.plot(np.sort(X, axis=0), est_gp.predict(np.sort(X, axis=0)), label='Symbolic Regression Fit', linewidth=2, color='red')
plt.xlabel('Solar Irradiance (kW/m2)')
plt.ylabel('Power output (kW)')
plt.legend(loc='upper left')
plt.show()