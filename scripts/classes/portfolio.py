import os
import pandas as pd
from pandas.io.pickle import to_pickle
import yfinance as yf
from datetime import datetime as dt

from equity import Equity

""" Portfolios are a Collection of Equity Objects.
    They can be created by passing in a list of tuples.
    The tuples either contain a string of a stock's symbol and the quantity of shares,
    or an Equity object and the quantity of shares

    If a list of Equities are passed in...
        - set the self.vars and you're done

    If a list of tuples are passed in...
        - Create a new list of tuples
        - Create the Equity Object
        - each new index is (Equity, Qty)


"""

class Portfolio:
    def __init__(self, symbols: list, parent_dir: str, start_dt: dt, endt_dt: dt, *interval: str) -> None:
        resp = 0

        if symbols == None:
            resp = -1
            print('Portfolio is Empty(NoneType)! Exiting...')
            exit()
        elif isinstance(symbols[0], tuple):
            self.parent_dir = parent_dir
            self.start = start_dt
            self.end = endt_dt
            self.interval = interval

            if isinstance(symbols[0][0], Equity):
                self.stocks = symbols
                resp = 1
            elif isinstance(symbols[0][0], str):
                self.stocks = []

                # TODO: create the equity objects
                for s in symbols:
                    e = Equity(s[0], self.parent_dir, self.start, self.end)
                    if isinstance(self.interval, str):
                        df = e.get_candles_one_interval(self.interval, self.start, self.end)
                        df.to_pickle(e.c_path + self.interval + '_'+ str((self.end-self.start).days) + 'd' +'.pkl')
                        resp = 1
                    else:
                        resp = e.get_all_candles()

                    self.stocks.append((e, s[1]))

            else:
                resp = -1
                print('Portfolio is Incorrect Type! Exiting...')
                exit()
        else:
            resp = -1
            print('Collection is incorrect type! Exiting...')
            exit()

        if resp == 1:
            print("Portfolio Initialized.")
        elif resp < 0:
            print("Error! Portfolio was not Initialized Correctly!")
            print(self.stocks)
            print(symbols)
            print("Exiting...")
            exit()
        else:
            print("Constructor Never Initialized! Exiting...")
            exit()
