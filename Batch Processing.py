def batch_process_data(df, batch_size=365):
    batches = [df[i:i + batch_size] for i in range(0, len(df), batch_size)]
    results = []
    for batch in batches:
        peaks = find_peaks(batch['INR to USD'].values)
        peak_dates = batch.index[peaks]
        results.append((peak_dates, batch['INR to USD'][peaks]))
    return results

# Example usage
batch_results = batch_process_data(df)
for i, (peak_dates, peak_values) in enumerate(batch_results):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['INR to USD'], label='INR to USD')
    plt.scatter(peak_dates, peak_values, color='red', label='Peaks')
    plt.title(f'Batch {i+1}: INR to USD Exchange Rate with Peaks')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.legend()
    plt.show()