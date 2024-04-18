
class Stock(list):
    def __init__(self, price):
        # super().__init__(price)  # Initialize the list
        self.price = price
        self.market_entry = self.best_market_entry()

    def best_market_entry(self):
        # Get the minimum price from to enter from last seven days.
        market_entry = min(self.price[:7])
        return market_entry
    def maximum_profit(self):
        profits = []
        for i in self.price[6:]:
            cum = i - self.market_entry
        profits.append(cum)
        print(max(profits))

price = [2, 5, 6, 7, 8, 9, 10, 11, 15, 17, 20, 6, 5, 12, 6, 3, 10, 18, 28]

entry = Stock(price)
print("Best entry is:", entry.best_market_entry())
print("Preceeding Prices are:", entry.maximum_profit())
