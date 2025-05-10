from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from datetime import datetime, timedelta
import pandas as pd
import requests
import os
"""
====================================================================================
DISCLAIMER - EDUCATIONAL USE ONLY
====================================================================================

This project is intended SOLELY for educational and research purposes.

By using or executing this code, you agree to the following terms:

- This project DOES NOT perform real trades, manage funds, or offer financial advice.
- The data used is fetched from Binance's public API and is subject to change.
- The author is NOT responsible for any loss, damage, or misinterpretation
  arising from the use or misuse of this code.
- DO NOT use this code with real money, real wallets, or live trading systems.
- This project is a SIMULATION TOOL for learning how financial data APIs work.

Use entirely at your own risk.

====================================================================================
"""
app = FastAPI()

def fetch_binance_klines(symbol, interval, start_time, end_time, limit=1000):
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': int(start_time.timestamp() * 1000),
        'endTime': int(end_time.timestamp() * 1000),
        'limit': limit
    }
    response = requests.get(url, params=params)
    data = response.json()
    if isinstance(data, dict) and "code" in data:
        raise Exception(f"Binance API hatası: {data}")
    return data

@app.get("/btc-minute-data-csv")
def get_btc_minute_data_csv(
    start: str = Query(..., description="Başlangıç tarihi (YYYY-MM-DD HH:MM)"),
    end: str = Query(..., description="Bitiş tarihi (YYYY-MM-DD HH:MM)")
):
    symbol = "BTCUSDT"
    interval = "1m"
    limit = 1000

    start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M")

    all_data = []
    current = start_dt

    while current < end_dt:
        next_time = min(current + timedelta(minutes=limit), end_dt)
        klines = fetch_binance_klines(symbol, interval, current, next_time, limit)
        if not klines:
            break
        all_data.extend(klines)
        last_ts = klines[-1][0] / 1000
        current = datetime.fromtimestamp(last_ts + 60)

    df = pd.DataFrame(all_data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'num_trades',
        'taker_buy_base', 'taker_buy_quote', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    EXPORT_DIR = "./exports"
    os.makedirs(EXPORT_DIR, exist_ok=True)

    filename = f"btc_{start_dt.strftime('%Y%m%d%H%M')}_{end_dt.strftime('%Y%m%d%H%M')}.csv"
    filepath = os.path.join(EXPORT_DIR, filename)

    df.to_csv(filepath, index=False)

    return FileResponse(filepath, media_type='text/csv', filename=filename)

@app.get("/eth-minute-data-csv")
def get_eth_minute_data_csv(
    start: str = Query(..., description="Başlangıç tarihi (YYYY-MM-DD HH:MM)"),
    end: str = Query(..., description="Bitiş tarihi (YYYY-MM-DD HH:MM)")
):
    symbol = "ETHUSDT"
    interval = "1m"
    limit = 1000

    start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M")

    all_data = []
    current = start_dt

    while current < end_dt:
        next_time = min(current + timedelta(minutes=limit), end_dt)
        klines = fetch_binance_klines(symbol, interval, current, next_time, limit)
        if not klines:
            break
        all_data.extend(klines)
        last_ts = klines[-1][0] / 1000
        current = datetime.fromtimestamp(last_ts + 60)

    df = pd.DataFrame(all_data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'num_trades',
        'taker_buy_base', 'taker_buy_quote', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    EXPORT_DIR = "./exports"
    os.makedirs(EXPORT_DIR, exist_ok=True)

    filename = f"eth_{start_dt.strftime('%Y%m%d%H%M')}_{end_dt.strftime('%Y%m%d%H%M')}.csv"
    filepath = os.path.join(EXPORT_DIR, filename)

    df.to_csv(filepath, index=False)

    return FileResponse(filepath, media_type='text/csv', filename=filename)

@app.get("/sol-minute-data-csv")
def get_sol_minute_data_csv(
    start: str = Query(..., description="Başlangıç tarihi (YYYY-MM-DD HH:MM)"),
    end: str = Query(..., description="Bitiş tarihi (YYYY-MM-DD HH:MM)")
):
    symbol = "SOLUSDT"
    interval = "1m"
    limit = 1000

    start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M")

    all_data = []
    current = start_dt

    while current < end_dt:
        next_time = min(current + timedelta(minutes=limit), end_dt)
        klines = fetch_binance_klines(symbol, interval, current, next_time, limit)
        if not klines:
            break
        all_data.extend(klines)
        last_ts = klines[-1][0] / 1000
        current = datetime.fromtimestamp(last_ts + 60)

    df = pd.DataFrame(all_data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'num_trades',
        'taker_buy_base', 'taker_buy_quote', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    EXPORT_DIR = "./exports"
    os.makedirs(EXPORT_DIR, exist_ok=True)

    filename = f"sol_{start_dt.strftime('%Y%m%d%H%M')}_{end_dt.strftime('%Y%m%d%H%M')}.csv"
    filepath = os.path.join(EXPORT_DIR, filename)

    df.to_csv(filepath, index=False)

    return FileResponse(filepath, media_type='text/csv', filename=filename)
