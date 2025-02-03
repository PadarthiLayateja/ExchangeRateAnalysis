def map_function(batch):
    peaks = find_peaks(batch['INR to USD'].values)
    peak_dates = batch.index[peaks]
    return peak_dates, batch['INR to USD'][peaks]

def reduce_function(batch_results):
    all_peaks = []
    for peak_dates, peak_values in batch_results:
        all_peaks.extend(zip(peak_dates, peak_values))
    return all_peaks

# Example usage
batches = [df[i:i + 365] for i in range(0, len(df), 365)]
mapped_results = [map_function(batch) for batch in batches]
reduced_results = reduce_function(mapped_results)

# Plot all peaks
peak_dates, peak_values = zip(*reduced_results)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['INR to USD'], label='INR to USD')
plt.scatter(peak_dates, peak_values, color='red', label='Peaks')
plt.title('INR to USD Exchange Rate with Peaks (MapReduce)')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.show()