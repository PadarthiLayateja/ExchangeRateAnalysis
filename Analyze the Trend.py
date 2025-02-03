import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('inr_usd_rates.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['INR to USD'], label='INR to USD')
plt.title('INR to USD Exchange Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.show()

# Find peaks
def find_peaks(data, window=5):
    peaks = []
    for i in range(window, len(data) - window):
        if data[i] > data[i - window:i].max() and data[i] > data[i + 1:i + window + 1].max():
            peaks.append(i)
    return peaks

peaks = find_peaks(df['INR to USD'].values)
peak_dates = df.index[peaks]

# Plot peaks
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['INR to USD'], label='INR to USD')
plt.scatter(peak_dates, df['INR to USD'][peaks], color='red', label='Peaks')
plt.title('INR to USD Exchange Rate with Peaks')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.show()