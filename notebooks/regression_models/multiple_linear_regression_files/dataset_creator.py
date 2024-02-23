# imports and configs:
import yfinance as yf
import pandas as pd
import datetime as dt

symbol = 'AMD'
end_dt = dt.datetime.today()
start_dt = end_dt - dt.timedelta(days=365*5)
export_path = '/Users/dB/Documents/repos/github/pythonic-finance/notebooks/regression_models/multiple_linear_regression_files/'

# Get FF Data
three_factor_coeffs = pd.read_csv('/Users/dB/.secret/ff-research-data/mlr/F-F_Research_Data_Factors_daily.CSV', index_col=0)
three_factor_coeffs.index = pd.to_datetime(three_factor_coeffs.index, format='%Y%m%d') # Format the date column(index) into a datetime object

five_factor_coeffs = pd.read_csv('/Users/dB/.secret/ff-research-data/mlr/F-F_Research_Data_5_Factors_2x3_daily.CSV', index_col=0)
five_factor_coeffs.index = pd.to_datetime(five_factor_coeffs.index, format='%Y%m%d') # Format the date column(index) into a datetime object

# Get Stock Data
stock = yf.download(symbol, start_dt, end_dt, interval='1d')
# Calculate Returns
stock['Ri'] = stock['Adj Close'].resample('1D').ffill().pct_change()
stock['Ri'] = stock['Ri']*100
stock = stock.dropna()
# Drop Extra Columns
returns = stock.drop(['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], axis=1)

# Concat the DFs
ff_3 = pd.concat([returns, three_factor_coeffs], axis=1)
ff_5 = pd.concat([returns, five_factor_coeffs], axis=1)


# Response Variables: Add 'y_' to the column names
ff_3['y_exp_return'] = ff_3['Ri']-ff_3['RF']
ff_5['y_exp_return'] = ff_5['Ri']-ff_5['RF']

# Predictor Variables: Add 'x_' to the column names
ff_3_df = ff_3.drop(['Ri', 'RF'], axis=1)
ff_5_df = ff_5.drop(['Ri', 'RF'], axis=1)

ff3_new_cols = {'Mkt-RF':'x_Mkt-RF', 'SMB':'x_SMB', 'HML':'x_HML'}
ff5_new_cols = {'Mkt-RF':'x_Mkt-RF', 'SMB':'x_SMB', 'HML':'x_HML', 'RMW':'x_RMW', 'CMA':'x_CMA'}

ff_3_df.rename(columns=ff3_new_cols, inplace=True)
ff_5_df.rename(columns=ff5_new_cols, inplace=True)

# Add Ones to a column for the Alpha Estimation
ff_3_df['x_ones'] = 1.0
ff_5_df['x_ones'] = 1.0

# Reorder the Columns
# 3-Factor: x_ones, x_Mkt-RF, x_SMB, x_HML, y_exp_return
ff3_reorder_into = ['x_ones', 'x_Mkt-RF', 'x_SMB', 'x_HML', 'y_exp_return']
ff3_final = ff_3_df[ff3_reorder_into]
# 5-Factor: x_ones, x_Mkt-RF, x_SMB, x_HML, x_RMW, x_CMA, y_exp_return
ff5_reorder_into = ['x_ones', 'x_Mkt-RF', 'x_SMB', 'x_HML', 'x_RMW', 'x_CMA', 'y_exp_return']
ff5_final = ff_5_df[ff5_reorder_into]

ff3_final.to_csv(export_path + 'ff_3_factor.csv')
ff5_final.to_csv(export_path + 'ff_5_factor.csv')

# Testing
print(ff3_final.head())
print(ff5_final.head())
