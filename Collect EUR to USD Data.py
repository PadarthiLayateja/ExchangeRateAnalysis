# Collect EUR to USD data
EUR_BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/history/USD/EUR/'

with open('eur_usd_rates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'EUR to USD'])
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        response = requests.get(EUR_BASE_URL + date_str)
        data = response.json()
        if 'conversion_rates' in data:
            eur_rate = data['conversion_rates']['EUR']
            writer.writerow([date_str, eur_rate])
        else:
            print(f"No data for {date_str}")
        current_date += delta

# Load EUR to USD data
eur_df = pd.read_csv('eur_usd_rates.csv', parse_dates=['Date'])
eur_df.set_index('Date', inplace=True)

# Plot EUR to USD data
plt.figure(figsize=(10, 6))
plt.plot(eur_df.index, eur_df['EUR to USD'], label='EUR to USD')
plt.title('EUR to USD Exchange Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.show()

# Find peaks in EUR to USD data
eur_peaks = find_peaks(eur_df['EUR to USD'].values)
eur_peak_dates = eur_df.index[eur_peaks]

# Plot peaks in EUR to USD data
plt.figure(figsize=(10, 6))
plt.plot(eur_df.index, eur_df['EUR to USD'], label='EUR to USD')
plt.scatter(eur_peak_dates, eur_df['EUR to USD'][eur_peaks], color='red', label='Peaks')
plt.title('EUR to USD Exchange Rate with Peaks')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.show()