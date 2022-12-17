import requests
import pandas as pd
from datetime import date
from datetime import timedelta
import seaborn as sns
import matplotlib.pyplot as plt

def get_currency_rates (from_currency, to_currency):
    '''
    Функция для получения курса валют за прошедшие 7 дней.
    Валюты принимаются на вход в виде трехбуквенных аббревиатур (согласно API fixer.io) 
    apikey - ключ получаем при регистрации на fixer.io
    end_date - сегодняшняя дата, например 2022-12-17
    start_date - дата 7 дней назад
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