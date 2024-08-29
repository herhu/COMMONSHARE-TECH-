import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class EagyBroker:
    def __init__(self):
        self.initial_prices = {'AMZN': random.uniform(100, 500), 'AAPLE': random.uniform(100, 500)}
        self.current_prices = {'AMZN': self.initial_prices['AMZN'], 'AAPLE': self.initial_prices['AAPLE']}
        self.total_bought = {'AMZN': 0, 'AAPLE': 0}
        self.total_sold = {'AMZN': 0, 'AAPLE': 0}
        self.history = {'AMZN': [], 'AAPLE': []}
        self.buy_signals = {'AMZN': [], 'AAPLE': []}
        self.sell_signals = {'AMZN': [], 'AAPLE': []}

        print(f"Initial Prices: AMZN = {self.initial_prices['AMZN']:.2f} USD, AAPLE = {self.initial_prices['AAPLE']:.2f} USD\n")

    def simulate_stock_exchange(self, symbol):
        try:
            shares_traded = random.randint(1, 1000)
            action = random.choice(['buy', 'sell'])

            if action == 'buy':
                self.total_bought[symbol] += shares_traded
            else:
                self.total_sold[symbol] += shares_traded

            # Update price after the total traded shares exceed 2000
            if self.total_bought[symbol] + self.total_sold[symbol] > 2000:
                total_trades = self.total_bought[symbol] + self.total_sold[symbol]
                p_I = self.total_sold[symbol] / total_trades  # Probability of price increase
                p_D = self.total_bought[symbol] / total_trades  # Probability of price decrease

                # Determine price movement
                if random.random() < p_I:
                    new_price = self.current_prices[symbol] * 1.1  # 10% increase
                    print(f"📈 Price Increase for {symbol}: p(I) = {p_I:.2f}")
                else:
                    new_price = self.current_prices[symbol] * 0.9  # 10% decrease
                    print(f"📉 Price Decrease for {symbol}: p(D) = {p_D:.2f}")

                print(f"\n🔄 Price Update for {symbol}:")
                print(f"Previous Price: {self.current_prices[symbol]:.2f} USD")
                print(f"New Price: {new_price:.2f} USD")
                print(f"Total Bought = {self.total_bought[symbol]}, Total Sold = {self.total_sold[symbol]}\n")

                self.current_prices[symbol] = new_price
                self.total_bought[symbol] = 0  # Reset after price update
                self.total_sold[symbol] = 0  # Reset after price update

                # Evaluate buy/sell decision
                self.evaluate(symbol)

            self.history[symbol].append(self.current_prices[symbol])

        except Exception as e:
            print(f"Error during stock exchange simulation for {symbol}: {e}")

    def evaluate(self, symbol):
        try:
            if self.current_prices[symbol] is None or self.initial_prices[symbol] is None:
                return

            price_diff = self.current_prices[symbol] - self.initial_prices[symbol]
            price_change_percentage = (price_diff / self.initial_prices[symbol]) * 100

            if price_change_percentage <= -10:
                print(f"🟢 Buy Signal for {symbol}: Current Price = {self.current_prices[symbol]:.2f} USD | Initial Price = {self.initial_prices[symbol]:.2f} USD | Price Change = {price_change_percentage:.2f}%\n")
                self.buy_signals[symbol].append(len(self.history[symbol]) - 1)
            elif price_change_percentage >= 10:
                print(f"🔴 Sell Signal for {symbol}: Current Price = {self.current_prices[symbol]:.2f} USD | Initial Price = {self.initial_prices[symbol]:.2f} USD | Price Change = {price_change_percentage:.2f}%\n")
                self.sell_signals[symbol].append(len(self.history[symbol]) - 1)

        except Exception as e:
            print(f"Error during evaluation for {symbol}: {e}")

def update(frame, broker, ax1, ax2):
    broker.simulate_stock_exchange('AMZN')
    broker.simulate_stock_exchange('AAPLE')

    ax1.clear()
    ax2.clear()

    ax1.plot(broker.history['AMZN'], label='AMZN', color='blue')
    ax2.plot(broker.history['AAPLE'], label='AAPLE', color='orange')

    # Mark buy and sell signals
    ax1.scatter(broker.buy_signals['AMZN'], [broker.history['AMZN'][i] for i in broker.buy_signals['AMZN']], color='green', label='Buy Signal')
    ax1.scatter(broker.sell_signals['AMZN'], [broker.history['AMZN'][i] for i in broker.sell_signals['AMZN']], color='red', label='Sell Signal')

    ax2.scatter(broker.buy_signals['AAPLE'], [broker.history['AAPLE'][i] for i in broker.buy_signals['AAPLE']], color='green', label='Buy Signal')
    ax2.scatter(broker.sell_signals['AAPLE'], [broker.history['AAPLE'][i] for i in broker.sell_signals['AAPLE']], color='red', label='Sell Signal')

    ax1.set_title('Real-Time Stock Price Simulation for AMZN')
    ax2.set_title('Real-Time Stock Price Simulation for AAPLE')
    ax1.set_ylabel('Stock Price (USD)')
    ax2.set_ylabel('Stock Price (USD)')
    ax1.legend()
    ax2.legend()

def main():
    try:
        broker = EagyBroker()
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

        ani = FuncAnimation(fig, update, fargs=(broker, ax1, ax2), interval=1000, cache_frame_data=False)

        plt.tight_layout()
        plt.show()

    except KeyboardInterrupt:
        print("\nProgram exited by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        plt.close('all')

if __name__ == "__main__":
    main()

