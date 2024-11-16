import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Data: Example dataset with a positive skew and high kurtosis
data = [3, 7, 8, 12, 13, 14, 18, 21, 24, 27, 40, 100]

# Calculate Skewness and Kurtosis
data_skewness = skew(data)
data_kurtosis = kurtosis(data, fisher=True)  # Fisher=True means excess kurtosis

# Display Results
print(f"Skewness: {data_skewness}")
print(f"Kurtosis (Excess): {data_kurtosis}")

# Detect Outliers (Using 1.5 * IQR Rule)
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = [x for x in data if x < lower_bound or x > upper_bound]

print(f"Outliers: {outliers}")

# Visualization: Histogram and Box-Plot
fig, axes = plt.subplots(2, 1, figsize=(8, 8))

# Histogram (Skewness Visualization)
axes[0].hist(data, bins=10, color='skyblue', edgecolor='black')
axes[0].axvline(np.mean(data), color='red', linestyle='--', label='Mean')
axes[0].axvline(np.median(data), color='green', linestyle='-', label='Median')
axes[0].set_title('Histogram: Skewness Visualization')
axes[0].legend()

# Box-Plot (Outliers and Spread)
axes[1].boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
axes[1].set_title('Box-Plot: Outliers and Spread')

plt.tight_layout()
plt.show()
