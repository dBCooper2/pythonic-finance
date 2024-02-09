import os
import pandas as pd
import yfinance as yf
import datetime as dt

""" Equities are a representation of a Stock. 
    they are an access point to pickle files of historical price and financial statement data.

    Pickle File Naming Conventions:
    
    All PKLs will be saved to self.parent_dir/self.symbol/...
        - .../candles/...
            - {symbol}_{interval}_{start_dt}_{end_dt}_candles.pkl
        - .../book/...
            - {symbol}_{year}__income_stmt.pkl
            - {symbol}_{year}_{quarter}_income_stmt_q.pkl
            - {symbol}_{year}__balance_sheet.pkl
            - {symbol}_{year}_{quarter}_balance_sheet_q.pkl
            - {symbol}_{year}__stmt_cash_flows.pkl
            - {symbol}_{year}_{quarter}_stmt_cash_flows_q.pkl
        - .../scraped/... This is data from Yahoo or TD Ameritrade/Schwab that has instrument data to check against
            - {symbol}_{date_accessed}_{Yahoo/TD}_stats.pkl

    Parameters:
    symbol - str : the stock's ticker symbol
    parent_dir - str : the parent directory that the Equity should store data in
"""
class Equity:
    def __init__(self, symbol: str, parent_dir: str) -> None:
        self.symbol = symbol
        self.parent_dir = parent_dir
        self.ticker = yf.Ticker(self.symbol)
        self.c_path = f'{self.parent_dir}/{self.symbol}/candles/' # candle data directory
        self.b_path = f'{self.parent_dir}/{self.symbol}/book/' # book data directory
        self.s_path = f'{self.parent_dir}/{self.symbol}/scraped/' # scraped data directory

    # Pull candle data from yfinance for all intervals as far back as possible
    def get_all_candles(self)-> None:
        pass

    # Used to get candles for a single equity at a specific interval, returns a DF of the candle data
    def get_candles_one_interval(self,interval: str, start_dt: dt, end_dt: dt)-> pd.DataFrame:
        df = yf.download(tickers=self.symbol, interval=interval, start=start_dt, end=end_dt)
        return df

    # pull book data from yfinance
    def get_book_data(self)-> None:
        pass