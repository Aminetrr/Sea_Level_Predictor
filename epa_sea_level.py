import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data
df = pd.read_csv('C:/Users/Lenovo/OneDrive/Bureau/EPA Sea Level/Sea_Level_Predictor/epa-sea-level.csv')

# Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Perform linear regression for the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years = pd.Series(range(1880, 2051))
sea_levels = intercept + slope * years
plt.plot(years, sea_levels, label='Best Fit Line 1880-2050', color='red')

# Perform linear regression from the year 2000
df_2000 = df[df['Year'] >= 2000]
slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
sea_levels_2000 = intercept_2000 + slope_2000 * years
plt.plot(years, sea_levels_2000, label='Best Fit Line 2000-2050', color='green')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save the plot
plt.savefig('sea_level_plot.png')

# Show the plot
plt.show()
