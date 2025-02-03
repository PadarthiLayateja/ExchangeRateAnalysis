import requests
import csv
from datetime import datetime, timedelta

# API Key (Replace with your actual API key)
API_KEY = 'YOUR_API_KEY'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/history/USD/INR/'

# Define the range of years
start_date = datetime(2020, 1, 1)
end_date = datetime.now()
delta = timedelta(days=1)

# Prepare CSV file
with open('inr_usd_rates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'INR to USD'])
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        response = requests.get(BASE_URL + date_str)
        data = response.json()
        if 'conversion_rates' in data:
            inr_rate = data['conversion_rates']['INR']
            writer.writerow([date_str, inr_rate])
        else:
            print(f"No data for {date_str}")
        current_date += delta