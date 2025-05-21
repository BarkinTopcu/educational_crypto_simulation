# 📊 Educational Crypto Forecasting & Auto-Buying Bot

This project demonstrates how to create a **basic forecasting and auto-buying simulation bot** using historical cryptocurrency data from Binance. It is specifically built for **educational and research purposes** only. The bot simulates how price forecasts can be used to make automatic simulated buy decisions for selected cryptocurrencies.

## 🚨 Disclaimer

> **⚠️ This project is strictly for educational use only.**
>
> - It is not intended for live or real-money trading.
> - It does not provide financial or investment advice.
> - The developer of this repository is not responsible for any financial loss resulting from the use or misuse of this code.
>
> Use this bot only in test environments or simulations. **Do not connect to real wallets or trading accounts.**
> 
> This application does not provide investment advice. All data, models, functions and forecasts are for educational and analytical purposes only. Do not use this information to make investment decisions. All investment decisions are the responsibility of the user.
> 
> **WARNING:** This application and all included analyses, data, and forecasts are strictly for educational and analytical purposes only. **Do not use for investment purposes under any circumstances.** The owner of the code assumes no responsibility for any financial, investment, or trading decisions made based on the information provided. **All responsibility lies with the user.**

> **ATTENTION:** In Turkey, investment transactions must only be carried out through intermediary institutions and financial organizations that are authorized and licensed by the Capital Markets Board of Turkey (CMB). This application or code should not be used for investment transactions and must not be considered for investment purposes.

---
---

### ⚠️ Yasal Uyarı (Türkçe)

❗️Bu proje **yatırım tavsiyesi değildir**.  
📌 Bu proje sadece **eğitim** amaçlı geliştirilmiştir.

- Herhangi bir finansal ya da yatırım tavsiyesi sunmaz.  
- Bu kodun kullanımından doğabilecek finansal kayıplardan geliştirici sorumlu değildir.  
- Bu bot sadece test ortamlarında veya simülasyonlarda kullanılmalıdır. Gerçek cüzdanlar veya ticaret hesapları ile **bağlantı kurmayınız**.
> Bu uygulama yatırım tavsiyesi içermez. Sunulan veriler, modeller, fonksiyonlar ve tahminler yalnızca eğitim ve analiz amaçlıdır. Yatırım kararlarınızı bu verilerle almanız önerilmez. Her türlü yatırım kararı kullanıcıya aittir.
> 
> **UYARI:** Bu uygulama ve içerdiği tüm analizler, veriler ve tahminler yalnızca eğitim ve analiz amaçlıdır. **Kesinlikle yatırım amaçlı kullanmayınız.** Uygulamada yer alan bilgilerle yapılacak herhangi bir yatırım, alım-satım veya finansal işlemden doğacak her türlü sorumluluk kullanıcıya aittir. **Kodun sahibi hiçbir şekilde sorumluluk kabul etmez.**

> **DİKKAT:** Türkiye’de yatırım işlemleri yalnızca Sermaye Piyasası Kurulu (SPK) tarafından yetkilendirilmiş ve lisanslanmış aracı kurumlar ve finansal kuruluşlar aracılığıyla yapılmalıdır. Bu uygulama veya kod, herhangi bir yatırım işlemi için kullanılmamalıdır ve yatırım amacıyla değerlendirilmemelidir.

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
## 🙋 FAQ

Q: Is this financial advice?

A: Absolutely not. It is purely a coding and learning exercise. It is for educational purpose.

## 📥 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/educational_crypto_bot.git
cd educational_crypto_bot


