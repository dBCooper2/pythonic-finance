# A Class for Simple Linear Regression using a DataFrame
import pandas as pd

class OLS_SimpleRegressionModel:
    def __init__(self, df: pd.DataFrame, learning_rate, num_iterations)-> None:
        self.df = df
        self.lr = learning_rate
        self.i = num_iterations

    def gradient_descent(m_current, b_current, self):
        m_gradient = 0
        b_gradient = 0

        n = len(self.df) # The number of rows in the dataset

        # Calculate the partial derivative summations
        for i in range(n):
            x = self.df.iloc[i].x
            y = self.df.iloc[i].y

            # These are a pythonic representation of partial derivative equations found in the theory section
            m_gradient += (-2/n) * x * (y - (m_current * x + b_current))
            b_gradient += (-2/n) * (y - (m_current * x + b_current))

        # Calculate the Gradient Descent equations from the theory section
        m = m_current - self.learning_rate * m_gradient
        b = b_current - self.learning_rate * b_gradient

        return m,b

    def run_regression(self):
        m = 0
        b = 0

        for i in range(self.num_iterations):
            m,b = self.gradient_descent(m, b)

        return m,b