from WebScraper import Ticker
from collections import deque #Double-Ended Queue
class PredictionAI:
    def __init__(self, ticker):
        self.ticker = ticker

    def fetch_data(ticker):
        ticker = Ticker(ticker)

        data = []
        for i in range(0,100):
            current_price = ticker.scrape()
            data.append(current_price)

        data = deque(data)

    def forecast(self):
        #Function for time-series forecasting using FBProphet
        pass

    def neural_network(self):
        #Create a tensorflow model(CNN)

        pass
