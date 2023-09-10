import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        result = getRatio(prices["ABC"], prices["DEF"])
        expected = ((121.2 + 120.48) / 2) / ((121.68 + 117.87) / 2)
        # print(result, expected)
        self.assertEqual(result, expected, msg="Unit Test 1 Failed")

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        result = getRatio(prices["ABC"], prices["DEF"])
        expected = ((119.2 + 120.48) / 2) / ((121.68 + 117.87) / 2)
        # print(result, expected)

        self.assertEqual(first=result, second=expected, msg="Unit Test 2 Failed")

    def test_getDataPoint_PriceBIsZero(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        result = getRatio(prices["ABC"], prices["DEF"])

        self.assertIsNone(result, msg="Unit Test 3 Failed")

    def test_getDataPoint_PriceAIsZero(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 133, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 123, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        result = getRatio(prices["ABC"], prices["DEF"])
        expected = 0

        self.assertEqual(expected,result, msg="Unit Test 4 Failed")

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_PriceAIsDoesntExist(self):
        quotes = [
            {'top_ask': {'price': 133, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 123, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        result = getRatio(None, prices["DEF"])

        self.assertIsNone(result, msg="Unit Test 5 Failed")

    """ ------------ Add more unit tests ------------ """
    def test_getDataPoint_PriceBIsDoesntExist(self):
        quotes = [
            {'top_ask': {'price': 133, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 123, 'size': 81}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        result = getRatio(prices["ABC"], None)

        self.assertIsNone(result, msg="Unit Test 6 Failed")

    """ ------------ Add more unit tests ------------ """


if __name__ == '__main__':
    unittest.main()
