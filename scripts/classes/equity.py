import os
import pandas as pd
from pandas.io.pickle import to_pickle
import yfinance as yf
from datetime import datetime as dt

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
    def __init__(self, symbol: str, parent_dir: str, start_dt: dt, end_dt: dt) -> None:
        self.symbol = symbol
        self.parent_dir = parent_dir
        self.start_dt = start_dt
        self.end_dt = end_dt

        self.ticker = yf.Ticker(self.symbol)
        self.c_path = f'{self.parent_dir}/{self.symbol}/candles/' # candle data directory
        self.b_path = f'{self.parent_dir}/{self.symbol}/book/' # book data directory
        self.s_path = f'{self.parent_dir}/{self.symbol}/scraped/' # scraped data directory

    # Pull candle data from yfinance for all intervals as far back as possible, return 1 if all PKLs are added, return -1 if a PKL is not able to be added
    def get_all_candles(self)-> int:
        intervals = pd.Series('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')

        count = 0
        for i in intervals:
            df = yf.download(self.ticker, start=self.start_dt, interval=intervals[i])

            df.filter(columns=['Date', 'Adj Close'])
            df.set_index(df['Date'], inplace=True)
            df = df.drop(columns='Date')
            df = df.rename(columns={'Adj Close':'Adj_Close'})

            if isinstance(df, pd.DataFrame):
                count+=1
                df.to_pickle(self.c_path + intervals[i] + '_'+ (self.end_dt-self.start_dt).days + 'd' +'.pkl')

        if count == len(intervals):
            return 1
        else:
            return -1

    # Used to get candles for a single equity at a specific interval, returns a DF of the candle data
    def get_candles_one_interval(self,interval: str, start_dt: dt, end_dt: dt)-> pd.DataFrame:
        df = yf.download(tickers=self.symbol, interval=interval, start=start_dt, end=end_dt)

        df.filter(columns=['Date', 'Adj Close'])
        df.set_index(df['Date'], inplace=True)
        df = df.drop(columns='Date')
        df = df.rename(columns={'Adj Close':'Adj_Close'})

        return df

    # pull book data from yfinance
    def get_book_data(self)-> None:
        i_s = self.ticker.income_stmt
        bs = self.ticker.balance_sheet
        cf = self.ticker.cashflow

        i_s_q = self.ticker.quarterly_income_stmt
        bs_q = self.ticker.quarterly_balance_sheet
        cf_q = self.ticker.quarterly_cashflow

        i_s.to_pickle(self.b_path + f'is_{(self.end_dt-self.start_dt).days}d.pkl')
        bs.to_pickle(self.b_path + f'bs_{(self.end_dt-self.start_dt).days}d.pkl')
        cf.to_pickle(self.b_path + f'cf_{(self.end_dt-self.start_dt).days}d.pkl')
        i_s_q.to_pickle(self.b_path + f'is_q_{(self.end_dt-self.start_dt).days}d.pkl')
        bs_q.to_pickle(self.b_path + f'bs_q_{(self.end_dt-self.start_dt).days}d.pkl')
        cf_q.to_pickle(self.b_path + f'cf_q_{(self.end_dt-self.start_dt).days}d.pkl')
