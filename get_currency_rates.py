import requests
import pandas as pd
from datetime import date
from datetime import timedelta
import seaborn as sns
import matplotlib.pyplot as plt

def get_currency_rates (from_currency, to_currency):
    '''
    Function to get exchange rates for the last seven days
    apikey - API key that you can get on fixer.io
    from_currency, to_currency - three-letter currency codes of your preferred base currency (see fixer.io API docs at https://fixer.io/documentation)
    end_date - today date, example: 2022-12-17
    start_date - date seven days before
    '''
    headers= {
        "apikey": "***"
            }
    end_date = date.today().strftime('%Y-%m-%d')
    start_date = (date.today()-timedelta(days=7)).strftime('%Y-%m-%d')
    query_string = f"?start_date={start_date}&end_date={end_date}&base={from_currency}&symbols={to_currency}"
    url = "https://api.apilayer.com/fixer/timeseries" + query_string
    return requests.get(url=url, headers=headers).json()

usd_eur = get_currency_rates('USD', 'EUR')
rub_eur = get_currency_rates('RUB', 'EUR')
df_usd_eur = pd.DataFrame(usd_eur['rates']).T.rename(columns={'EUR':'USD-EUR'})
df_rub_eur = pd.DataFrame(rub_eur['rates']).T.rename(columns={'EUR':'RUB-EUR'})
df_merged = df_usd_eur.join(df_rub_eur)
df_merged.to_csv('currency_rates.csv')