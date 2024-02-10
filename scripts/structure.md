# Structure of Scripts

This repository should be a modular series of scripts where a new method of analyzing equities can be added without significant changes needed. This was a big issue with the dBI project and I hope to improve it here.

## Current Plans

The scripts should be able to perform analysis to decide if an equity is a good addition to a portfolio. This means that for each model, it needs to be able to function with both a single security or with a portfolio of securities. 

The current scripts should be able to analyze a portfolio and a series of prospective additions to the portfolio using CAPM and Fama-French Models. This means the structure for the project should look like:

### __Equity__

- A class describing a single asset, containing historical price(candle) data and financial statement(book) data.

- \_\_init\_\_() passes in a file path, start date, end date, sampling frequency, and a stock symbol, and creates a yf Ticker that can be called to create PKL files of the necessary data in repository within that file path

### __Portfolio__

- A class describing a Collection of entities that reference the individual Entity objects

- \_\_init\_\_() passes in a list of symbols, start date, end date, sampling frequency, and a file path, and the portfolio constructor first checks the file path to see what exists inside of the path, then fills the repository with the remaining necessary PKL files. The item stored in the Portfolio Object is a Collection of Equity Objects

### __OLS_Simple_Linear_Regression__

- An abstract superclass that is a linear regression model, with the ability for either univariate or multivariate linear regression

- \_\_init\_\_() passes in a DataFrame containing the relevant X and Y data for the Regression Model as well as a Learning Rate and a Number of Iterations that the ML Model should train on

- The linear regression functions should be performed in the superclass, with the subclasses only adding a custom ANOVA table that is specific to the type of analysis being performed.

- Functions:
  - Gradient Descent
  - Error/Loss/Cost Function
  - Iterative Regression Function
  - ANOVA Table Generator

### __CAPM_Regression__

- extends Linear_Regression for Single-Variable regression on a single asset/portfolio

- Inherited Functions:
  - Gradient Descent
  - Error/Loss/Cost Function
  - Iterative Regression Function

- Overidden Functions
  - ANOVA Table Generator


### __FF_Regression__

- extends Linear_Regression for Multiple Variable regression on a single asset/portfolio, with the ability to do the 3-factor or 5-factor models

- Inherited Functions:
  - Gradient Descent
  - Error/Loss/Cost Function
  - Iterative Regression Function
  
- Overidden Functions
  - ANOVA Table Generator
