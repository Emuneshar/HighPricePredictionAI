from WebScraper import Ticker
from fbprophet import Prophet
import pandas as pd
import numpy as np
from stocker import Stocker


class PredictionAI:
    def __init__(self, ticker):
        self.ticker = ticker

    def fetch_data(ticker):
        ticker = Ticker(ticker)

        data = []
        for i in range(0,100):
            current_price = ticker.scrape()
            data.append(current_price)


    def prophet(self, data):
        data = pd.Dataframe(data)
        data.columns("Price")

        m = Prophet()
        m.fit(data)

        future = m.make_future_dataframe(periods=365)
        forecast = m.predict(future)

        fig1 = m.plot(forecast)

        def components():
            fig2 = m.plot_components(forecast)

    class Forecast:
        def __init__(self, ticker_symbol):
            self.stock = Stocker(ticker_symbol)

        def price_history(self):
            self.stock.plot_stock()

        def model(self):
            model, model_data = self.stock.create_prophet_model(days=90)

        def prediction(self):
            self.stock.evaluate_prediction()

        def prediction_with_shares(self, shares):
            self.stock.evaluate_prediction(nshares=shares)

        def predict_future(self, days):
            self.stock.predict_future(days=days)

    def neural_network(self):
        #TODO: Create a tensorflow model(CNN)

        pass
