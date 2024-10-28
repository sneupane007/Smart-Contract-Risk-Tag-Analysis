import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pointbiserialr
import scipy.stats

# Load the dataset
df = pd.read_excel('/compiled_risk_data.xlsx')

# Drop the first five colums irrelevant to our analysis
df = df.drop(df.columns[:5], axis=1)
# Calculate the frequency of 'True' values for each risk tag
# Calculate the frequency of 'True' values for each risk tag
frequencies = df.apply(lambda x: x.value_counts().get(True, 0))
print("Frequency of 'True' for each risk tag:")
print(frequencies)

# Calculate total entries for percentage calculation
total_entries = len(df)
percentages = (frequencies / total_entries) * 100
frequency_df = pd.DataFrame({
    'Risk Tag': frequencies.index,
    'Frequency of True': frequencies.values,
    'Percentage of True': percentages.values
})
print(frequency_df)

#Plot the frequency chart
plt.figure(figsize=(18, 6))

colors = ['green' if freq < 100 else 'yellow' if freq < 200 else 'red' for freq in frequency_df['Frequency of True']]

sns.barplot(x=frequency_df['Risk Tag'], y=frequency_df['Frequency of True'], palette = colors)
plt.title('Frequency of True Values for Each Risk Tag')
plt.xlabel('Risk Tags')
plt.ylabel('Frequency of True')
plt.xticks(rotation=90)
plt.show()

def phi_coefficient(x, y):
    """Calculate the Phi coefficient for two binary variables."""
    contingency_table = pd.crosstab(x, y)
    chi2 = scipy.stats.chi2_contingency(contingency_table, correction=False)[0]
    n = np.sum(contingency_table.values)
    phi = np.sqrt(chi2 / n)
    return phi

# Calculate the Phi coefficient for each pair of binary variables
binary_variables = df.columns[df.dtypes == 'bool']
phi_matrix = pd.DataFrame(index=binary_variables, columns=binary_variables)

for var1 in binary_variables:
    for var2 in binary_variables:
        phi_matrix.loc[var1, var2] = phi_coefficient(df[var1], df[var2])

phi_matrix = phi_matrix.astype(float)  # Convert to float for correct heatmap display
print(phi_matrix)

#Plot the heat map
plt.figure(figsize=(18, 15))
sns.heatmap(phi_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Phi Coefficient Heatmap of Risk Tags')
plt.show()
