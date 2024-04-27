import csv
import random
import string
from datetime import datetime, timedelta

# List of cost center names
cost_center_names = ['Marketing Operations', 'IT Infrastructure', 'Human Resources', 'Sales Operations', 'Finance', 'Research & Development']

# List of regions
regions = ['North America', 'Europe', 'Asia Pacific', 'South America']

# List of cost categories
cost_categories = ['Advertising', 'Hardware', 'Salaries', 'Travel', 'Professional Services', 'Supplies', 'Software', 'Benefits', 'Commissions']

# List of currency codes
currency_codes = ['USD', 'EUR', 'JPY', 'BRL', 'GBP', 'SGD', 'ARS']

# Function to generate a random cost center number
def generate_cost_center_number():
    return random.randint(1000, 9999)

# Function to generate a random timestamp
def generate_timestamp(start_date, end_date):
    start = start_date
    end = end_date
    random_date = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return random_date.strftime('%Y-%m-%d %H:%M:%S')


# Open the CSV file for writing
with open('/Users/admiral/Documents/GitHub/conversational-analytics/scripts/sample-data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Cost center number', 'Cost center name', 'Region', 'Cost category', 'timestamp', 'currency code', 'amount'])

    # Generate and write 1000 records
    for _ in range(1000):
        cost_center_number = generate_cost_center_number()
        cost_center_name = random.choice(cost_center_names)
        region = random.choice(regions)
        cost_category = random.choice(cost_categories)
        timestamp = generate_timestamp(datetime(2023, 8, 1), datetime(2023, 8, 4))
        currency_code = random.choice(currency_codes)
        amount = random.randint(1000, 1000000)

        writer.writerow([cost_center_number, cost_center_name, region, cost_category, timestamp, currency_code, amount])

print("Sample data generated and saved to 'sample_data.csv'")



