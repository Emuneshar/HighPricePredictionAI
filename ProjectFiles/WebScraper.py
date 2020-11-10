from bs4 import BeautifulSoup
from selenium import webdriver

class Scraper:
    
    def __init__(self, ticker):
        self.ticker = ticker
    
    def firefox(ticker):
        driver = None

        try:
            driver = webdriver.Firefox()
            driver.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
            soup = BeautifulSoup(driver.page_source, "lxml")
            item = soup.find(id = "quote-market-notice").find_parent().find("span").text
            
            print(item)
            driver.quit()

        except Exception as e:
            try:
                chrome(self.ticker)
            
            except Exception as e:
                print("Error")


    def chrome(ticker):
        driver = None

        try:
            driver = webdriver.Chrome()
            driver.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
            soup = BeautifulSoup(driver.page_source, "lxml")
            item = soup.find(id = "quote-market-notice").find_parent().find("span").text
            
            print(item)
            driver.quit()

        except Exception as e:
            try:
                firefox(self.ticker)

            except Exception as e:
                print(Error)

