from WebScraper import Ticker
from fbprophet import Prophet
import pandas as pd
import numpy as np


class PredictionAI:
    def __init__(self, ticker):
        self.ticker = ticker

    def fetch_data(ticker):
        ticker = Ticker(ticker)

        data = []
        for i in range(0,100):
            current_price = ticker.scrape()
            data.append(current_price)


    def forecast(self, data):
        data = pd.Dataframe(data)
        data.columns("Price")

        m = Prophet()
        m.fit(data)

        future = m.make_future_dataframe(periods=365)
        forecast = m.predict(future)

        fig1 = m.plot(forecast)

        def components():
            fig2 = m.plot_components(forecast)

    def neural_network(self):
        #TODO: Create a tensorflow model(CNN)

        pass
