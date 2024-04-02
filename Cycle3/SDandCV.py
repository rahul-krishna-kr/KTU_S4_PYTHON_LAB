'''  
1. Import Library:

Import the Pandas library (pd) using import pandas as pd. This library provides data manipulation functionalities.
2. Prepare Data:

Create a list of lists named data to store the table data (if applicable).
Each inner list represents a row in the table, containing elements for "Class", "Frequency", and "f(x)".
Populate the data list with the values from your table.
3. Create DataFrame (if using data list):

If you prepared the data in a list of lists (data), use pd.DataFrame(data, columns=["Class", "Frequency", "f(x)"]) to construct a Pandas DataFrame named df.
data: The list of lists containing the table data.
columns=["Class", "Frequency", "f(x)" ]: Defines the column names for the DataFrame.
If your data is in a different format (like a CSV file), skip this step and proceed to loading the data from the external source (explained later).
4. Load Data from External Source (if not using data list):

If your data resides in a CSV file or another format, use Pandas functions like pd.read_csv to read the data into a DataFrame named df.
Replace the DataFrame creation step (point 3) with the appropriate function call to load your specific data format.
Ensure the loaded DataFrame has columns named "Class", "Frequency", and "f(x)" (or adjust the column names in subsequent steps if they differ).
5. Calculate Mean of f(x):

Calculate the average value in the "f(x)" column.
Use df['f(x)'].mean() to find the mean and store it in a variable like mean_f_x.
6. Calculate Squared Deviations:

Create a new column named "Squared Deviation" to hold the squared deviations from the mean for each "f(x)" value.
Use df['Squared Deviation'] = (df['f(x)'] - mean_f_x) ** 2 to calculate the squared difference between each "f(x)" value and the mean.
7. Calculate Standard Deviation:

Calculate the standard deviation, which measures the spread of data around the mean.
Find the average of the squared deviations using df['Squared Deviation'].mean().
Raise this result to the power of 0.5 (square root) using ** 0.5 to get the standard deviation and store it in standard_deviation.
8. Calculate Coefficient of Variation (C.V.):

The C.V. expresses the standard deviation as a percentage of the mean.
Calculate coefficient_variation = (standard_deviation / mean_f_x) * 100.
Multiply the result by 100 to express it as a percentage.
9. Print Results:

Print the calculated standard deviation and coefficient of variation with a percentage sign using print statements
'''

import pandas as pd

# Class data (assuming data is available in a list of lists)
data = [
    [0, 10, 5],
    [10, 20, 10],
    [20, 30, 20],
    [30, 40, 40],
    [40, 50, 30],
    [50, 60, 20],
    [60, 70, 10],
    [70, 80, 5],
]

# Create DataFrame from the data
df = pd.DataFrame(data, columns=["Class", "Frequency", "f(x)"])

# Calculate mean of f(x)
mean_f_x = df['f(x)'].mean()

# Calculate squared deviations from the mean
df['Squared Deviation'] = (df['f(x)'] - mean_f_x) ** 2

# Calculate standard deviation
standard_deviation = df['Squared Deviation'].mean() ** 0.5

# Calculate coefficient of variation
coefficient_variation = (standard_deviation / mean_f_x) * 100

# Print results
print("Standard Deviation:", standard_deviation)
print("Coefficient of Variation (C.V.):", coefficient_variation, "%")
