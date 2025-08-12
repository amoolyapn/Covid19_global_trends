import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load(file):
    # Load data, group by country, drop Lat/Long, convert all columns to numeric
    df = pd.read_csv(file).groupby('Country/Region').sum().drop(['Lat', 'Long'], axis=1)
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)  # Convert to numeric and fill NaNs
    return df

# Load datasets
confirmed = load('time_series_covid19_confirmed_global.csv')
deaths = load('time_series_covid19_deaths_global.csv')
recovered = load('time_series_covid19_recovered_global.csv')
