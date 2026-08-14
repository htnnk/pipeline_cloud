import os
import requests
import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:1tdfVTKu1K4qyQLt@db.lktgjycvfmmpqlsalhth.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)

# -- test --
data_inicio = '2026-08-01'
hoje = pd.Timestamp.now()

ativos = ["ITUB3.SA", "VALE3.SA", "PETR3.SA", "^BVSP"]

# Add interval='1h' here to pull hourly bars
df = yf.download(ativos, start=data_inicio, end=hoje, interval='1h')['Close']

# Rest of your transformation logic
df_unpivoted = df.reset_index()

df_final = df_unpivoted.melt(
    id_vars=['Datetime'],  # yfinance names intraday timestamp column 'Datetime' (or 'Date')
    var_name='ticker', 
    value_name='preco_fechamento'
)

df_final.columns = ['Data', 'ticker', 'preco_fechamento']
df_final['Data'] = pd.to_datetime(df_final['Data']).dt.strftime('%Y-%m-%d %H:%M')
df_final = df_final.dropna()

df_final.to_sql('stock_prices', engine, if_exists='append', index=False)

print('Data successfully uploaded to Supabase!')

print(df_final)