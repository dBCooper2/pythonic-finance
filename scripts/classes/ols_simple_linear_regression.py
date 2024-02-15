import pandas as pd
import numpy as np


class OLS_Simple_Linear_Regression:
    def __init__(self, df: pd.DataFrame, learning_rate: int, num_iterations: int) -> None:
        self.df = df
        self.lr = learning_rate
        self.ni = num_iterations
        self.ns = len(df.columns.tolist()) - 1 # This is the number of predictor coefficients(all the X's in the DF and exclude the 1 Y)

    # the slopes passed in need to be an array because the number of coeffs for Multiple Linear Regression is indeterminate
    def gradient_descent(self, m_curr_arr: list, b_curr: float):
        pass

    # TODO: Determine how this table should be created. Should I update this with each iteration or create the table all at once at the end of the regression?
    def create_or_update_anova_table(self):
        pass

    def ols_regression(self):
        m=np.zeros(self.ns,dtype=np.float64)
        b=0.0

        for i in self.ni:
            m,b = self.gradient_descent(m.tolist(), b)
            self.create_or_update_anova_table() # Should this go here?
        pass