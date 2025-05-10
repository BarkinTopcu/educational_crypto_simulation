# 📊 Educational Crypto Forecasting & Auto-Buying Bot

This project demonstrates how to create a **basic forecasting and auto-buying simulation bot** using historical cryptocurrency data from Binance. It is specifically built for **educational and research purposes** only. The bot simulates how price forecasts can be used to make automatic simulated buy decisions for selected cryptocurrencies.

## 🚨 Disclaimer

> **⚠️ This software is strictly for educational use only.**
>
> - It is not intended for live or real-money trading.
> - It does not provide financial or investment advice.
> - The developer of this repository is not responsible for any financial loss resulting from the use or misuse of this code.
>
> Use this bot only in test environments or simulations. **Do not connect to real wallets or trading accounts.**

---

## 📌 Project Overview

This educational bot fetches candlestick (OHLC) data from the Binance public API and applies forecasting models to predict future price trends. Based on the prediction output and a simple rule-based logic, it simulates a "buy" decision.

### Supported Coins:
- Bitcoin (BTC/USDT)
- Ethereum (ETH/USDT)
- Solana (SOL/USDT)

### Data Source:
- Binance Kline (candlestick) endpoint:  
  `https://api.binance.com/api/v3/klines`

---

## 🔧 Features

- 📈 **Forecasting** using selected time series models
- 🤖 **Auto-buy simulation** based on configurable strategy thresholds
- 🧪 **Backtesting capability** for performance evaluation
- 📚 **Educational commentary** throughout the code

---

## 🧠 Learning Objectives

This project is intended to help students or data enthusiasts:

- Understand the structure of crypto market data (OHLCV)
- Learn how to use public APIs to retrieve financial data
- Explore basic forecasting techniques
- Simulate rule-based trading logic
- Develop ethical and cautious approaches to algorithmic trading

---
##🙋 FAQ
Q: Is this financial advice?
A: Absolutely not. It is purely a coding and learning exercise. It is for educational purpose.

## 📥 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/educational_crypto_bot.git
cd educational_crypto_bot


