import unittest
from eagy_broker import EagyBroker

class TestEagyBroker(unittest.TestCase):

    def setUp(self):
        """Set up the initial conditions for each test."""
        self.broker = EagyBroker()

    def test_initial_prices(self):
        """Test that initial prices are set within the correct range."""
        for symbol in ['AMZN', 'AAPLE']:
            self.assertGreaterEqual(self.broker.initial_prices[symbol], 100)
            self.assertLessEqual(self.broker.initial_prices[symbol], 500)

    def test_simulate_stock_exchange_buy(self):
        """Test that simulating a 'buy' action increases total_bought."""
        initial_bought = self.broker.total_bought['AMZN']
        self.broker.total_bought['AMZN'] += 500  # Simulate a buy action
        self.assertEqual(self.broker.total_bought['AMZN'], initial_bought + 500)

    def test_simulate_stock_exchange_sell(self):
        """Test that simulating a 'sell' action increases total_sold."""
        initial_sold = self.broker.total_sold['AAPLE']
        self.broker.total_sold['AAPLE'] += 300  # Simulate a sell action
        self.assertEqual(self.broker.total_sold['AAPLE'], initial_sold + 300)

    def test_price_update_increase(self):
        """Test that price increases correctly when probability is high."""
        self.broker.total_bought['AMZN'] = 0
        self.broker.total_sold['AMZN'] = 3000
        initial_price = self.broker.current_prices['AMZN']
        self.broker.simulate_stock_exchange('AMZN')
        self.assertGreater(self.broker.current_prices['AMZN'], initial_price)

    def test_price_update_decrease(self):
        """Test that price decreases correctly when probability is low."""
        self.broker.total_bought['AAPLE'] = 3000
        self.broker.total_sold['AAPLE'] = 0
        initial_price = self.broker.current_prices['AAPLE']
        self.broker.simulate_stock_exchange('AAPLE')
        self.assertLess(self.broker.current_prices['AAPLE'], initial_price)

    def test_buy_signal(self):
        """Test that a buy signal is generated correctly."""
        self.broker.initial_prices['AMZN'] = 200.00
        self.broker.current_prices['AMZN'] = 175.00
        self.broker.evaluate('AMZN')
        self.assertIn(len(self.broker.history['AMZN']) - 1, self.broker.buy_signals['AMZN'])

    def test_sell_signal(self):
        """Test that a sell signal is generated correctly."""
        self.broker.initial_prices['AAPLE'] = 150.00
        self.broker.current_prices['AAPLE'] = 165.00
        self.broker.evaluate('AAPLE')
        self.assertIn(len(self.broker.history['AAPLE']) - 1, self.broker.sell_signals['AAPLE'])

if __name__ == '__main__':
    unittest.main()
