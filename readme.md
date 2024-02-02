# Pythonic Finance - Financial Engineering/Analysis in Python

Statistical Analysis of Equities using Time Series Models, Regression, the Capital Asset Pricing Model(CAPM), and the Fama French 3-Factor and 5-Factor Models in Python and iPython Notebooks.

I will be taking notes on the Textbook _Statistics and Data Analysis for Financial Engineering with R examples_, and use it as a reference to learn about financial engineering and translate it into Python code and iPython notebooks.

## Python Scripts

Scripts will be written as/after I finish sections of the textbook, and will focus on Object-Oriented representations of the finance topics covered in the Jupyter/iPython Notebooks

If you are interested in previous projects I have written that cover similar topics, please take a look at:

[CAPM](https://github.com/dBCooper2/financial-modeling/blob/main/notebooks/finance/capm.ipynb) and [Fama-French](https://github.com/dBCooper2/financial-modeling/blob/main/notebooks/finance/fama-french.ipynb) Beta Estimation in Jupyter Notebooks

[Scraping Data from Yahoo Finance](https://github.com/dBCooper2/financial-modeling/blob/main/notebooks/data_processing/yahoo_finance_scraper.ipynb)

Visualizing [Candle](https://github.com/dBCooper2/financial-modeling/blob/main/notebooks/finance/mpl_finance_visualizations.ipynb) and [Financial Statement](https://github.com/dBCooper2/financial-modeling/blob/main/notebooks/finance/visualizing_book_data.ipynb) Data

## Jupyter/iPython Notebooks

### _Textbook Notes:_ [Calculating Returns](notebooks/financial_data/returns_textbook_notes.ipynb)

<img src="/docs/readme_files/returns_chapter/amd_log_returns.png" alt="amd_log" style="width: 85%;"/>

This notebook examines the calculation of Net, Gross and Log Returns of an asset, along with how and why they are used. Included is a comparison of 3 semiconductor equities, ADI, AMAT and AMD, as well as a simple time series for each stock's logarithmic returns over a 5-year period.

### _Textbook Notes:_ [Time Series Modeling](notebooks/time_series/)

### _Textbook Notes:_ [Examining Distributions](notebooks/time_series/exploratory_data_analysis.ipynb)

<img src="/docs/readme_files/time_series_data_analysis_chapter/dists_side_by_side.png" alt="dists_compared"/>

This notebook covers a wide array of data analysis techniques for assets: Sample Quantiles, Kernel Density Estimations, Tests of Normality are some of the functions in this notebook; The plots covered are Histograms, Box Plots, Normal Probability Plots, Half-Normal Plots, and Quantile-Quantile Plots.

Included are histograms and Normal Probability Plots of the semiconductor stock APH's daily adjusted close price, net returns, log returns and root returns.

_Note: The Python section of this notebook is still in-progress, as a result this notebook is mostly just notes in markdown and LaTeX. The functions will be done before 2/4/24_

### _Textbook Notes:_ Time Series Modeling: Basics

### _Textbook Notes:_ Time Series Modeling: Further Topics

### _Textbook Notes:_ Modeling Univariate and Multivariate Statistical Models

### _Textbook Notes:_ Regression Models

### _Textbook Notes:_ GARCH Models

### _Textbook Notes:_ Portfolio Selection

### _Textbook Notes:_ Capital Asset Pricing Model

### Fama-French 3-Factor Model

### Fama-French 5-Factor Model

### Portfolio Evaluation and Comparison Measures

### Custom Regression Models for CAPM and FF3/FF5 Models

## Resources

Ruppert, David and David S. Matteson. _Statistics and Data Analysis for Financial Engineering with R examples_. $2^{nd}$ ed., Springer, 2015.

Quantivity. "Why Log Returns?" Quantivity, 21 Feb. 2011, <https://quantivity.wordpress.com/2011/02/21/why-log-returns/>.

Costan, Julian. "Linear vs. Log Returns." Decentralized Meta-Learning, 14 Sept. 2021, <https://blog.costan.ro/post/2021-09-14-linear-log-returns/>.

Hudson, Robert and Gregoriou, Andros, _Calculating and Comparing Security Returns is Harder than you Think: A Comparison between Logarithmic and Simple Returns_ (February 7, 2010). Available at SSRN: <https://ssrn.com/abstract=1549328>

Meucci, Attilio, _Quant Nugget 2: Linear vs. Compounded Returns – Common Pitfalls in Portfolio Management_ (May 1, 2010). GARP Risk Professional, pp. 49-51, April 2010 , Available at SSRN: <https://ssrn.com/abstract=1586656>
