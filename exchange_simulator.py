# exchange_simulator.py
"""
### ⚠️ Disclaimer / Sorumluluk Reddi

**English:**  
This application is developed for educational purpose only. It does **not** provide financial or investment advice. All investment decisions made based on this application are at the sole discretion and risk of the user. The developer assumes **no responsibility** for any financial loss or damage resulting from the use of this tool.

**Türkçe:**  
Bu uygulama yalnızca eğitim amaçlı geliştirilmiştir. **Yatırım tavsiyesi niteliği taşımaz.** Uygulama aracılığıyla yapılan tüm yatırım kararları tamamen kullanıcının kendi inisiyatifinde ve sorumluluğundadır. Uygulamanın geliştiricisi, kullanım sonucu oluşabilecek hiçbir maddi zarardan **sorumlu değildir.**
"""
class ExchangeSimulator:
    def __init__(self, initial_balance: float, porfolio:dict = None, ):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.portfolio = porfolio
        self.trade_history = []  # list of tuples: (type, symbol, amount, price)
        self.current_prices = {}  # {'BTC': current_price}

    def update_price(self, symbol: str, price: float):
        self.current_prices[symbol] = price

    def buy(self, symbol: str, amount: float):
        price = self.current_prices.get(symbol)
        if price is None:
            raise ValueError(f"Price for {symbol} not available.")
        cost = amount * price
        if cost <= self.balance:
            self.balance -= cost
            self.portfolio[symbol] = self.portfolio.get(symbol, 0) + amount
            self.trade_history.append(('BUY', symbol, amount, price))
            return "Succesfull Buy"
        else:
            return "Unsuccess: Insufficient Money"

    def sell(self, symbol: str, amount: float):
        if self.portfolio.get(symbol, 0) >= amount:
            price = self.current_prices.get(symbol)
            if price is None:
                raise ValueError(f"Price for {symbol} not available.")
            revenue = amount * price
            self.portfolio[symbol] -= amount
            self.balance += revenue
            self.trade_history.append(('SELL', symbol, amount, price))
            return "Succesfull Sell"
        else:
            return "Unsuccess Sell"

    def get_portfolio(self):
        return dict(self.portfolio)

    def get_balance(self):
        return round(self.balance, 2)

    def get_trade_history(self):
        return list(self.trade_history)

    def reset(self):
        self.balance = self.initial_balance
        self.portfolio = {}
        self.trade_history = []
