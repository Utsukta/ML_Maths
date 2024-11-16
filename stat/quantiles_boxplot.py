import numpy as np
import matplotlib.pyplot as plt

# Data
data = [3, 7, 8, 12, 13, 14, 18, 21, 24, 27]

# Calculate Quartiles
Q1 = np.percentile(data, 25)  # 25th Percentile
Q2 = np.percentile(data, 50)  # 50th Percentile (Median)
Q3 = np.percentile(data, 75)  # 75th Percentile

# Display Quartile Results
print(f"Q1 (25th Percentile): {Q1}")
print(f"Q2 (Median, 50th Percentile): {Q2}")
print(f"Q3 (75th Percentile): {Q3}")

# Interquartile Range (IQR)
IQR = Q3 - Q1
print(f"IQR (Q3 - Q1): {IQR}")

# Box-Plot Visualization
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title("Box-Plot of Data")
plt.xlabel("Value")
plt.show()
