
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('website_traffic_data.csv')

# Print basic statistics
print("Summary statistics:")
print(df.describe())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot traffic trends
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['PageViews'], marker='o', label='PageViews')
plt.plot(df['Date'], df['UniqueVisitors'], marker='s', label='Unique Visitors')
plt.title('Website Traffic Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
