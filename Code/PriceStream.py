from WebScraper import Ticker
import time
import threading

class Test_Thread(threading.Thread):
    def __init__(self, ticker):
        threading.Thread.__init__(self)
        self.ticker = ticker

    def run(self):
        ticker = Ticker(self.ticker)
        price = ticker.scrape()

        while(True):
            print(price)
            time.sleep(1)

t = Test_Thread("GOOG")
t.start()
