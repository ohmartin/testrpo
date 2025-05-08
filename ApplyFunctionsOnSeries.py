import pandas as pd
import numpy as np

cars_data = pd.read_csv("C:\\Users\\213356\\OneDrive - MyFedEx\\PILOT\\Training\\Python\\Training\\ZoomCars.csv")

cars_data = cars_data.drop(columns=['id','url','page','fetched', 'price_currency',
                                    'ad_id', 'location', 'description'])

cars_data = cars_data.dropna()
cars_data = cars_data.reset_index()
cars_data = cars_data.drop(['index'], axis=1)

changeCase = lambda x : x.upper()
cars_data['import'] = cars_data['current_location'].map(
                    {'In Tanzania' : 'No',
                     'Available For Import': 'Yes'}
)

def drop_comma(x):
    return str(x).replace(',','')
cars_data['price_value'] = cars_data['price_value'].apply(drop_comma)
cars_data['price_value'] = pd.to_numeric(cars_data['price_value'])

def category(price):
    price=int(price)

    if price <= 10000000:
        return 'cheap'
    elif price > 10000000 and price <= 30000000:
        return 'mid-range'
    elif price > 30000000 and price <= 70000000:
        return 'expensive'
    else:
        return 'luxury'
cars_data['price_range'] = cars_data.price_value.apply(category)
print(cars_data)
