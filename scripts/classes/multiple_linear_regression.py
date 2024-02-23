import numpy as np
import pandas as pd

# DataFrame Columns must be labeled as 'x_<name>' or 'y_name' for the regression model to work
class MultipleLinearRegression:
    def __init__(self, df: pd.DataFrame) -> None:
        self.x = df.filter(like='x_').dropna().values
        self.y = df.filter(like='y_').dropna().values

        if self.x.shape == self.y.shape:
            print('Model Initialized Correctly.')
            self.betas = self.normal_equation_estimation(self.x, self.y)
        else:
            print('Model Shapes are Incorrect, check that what is being passed through is correct. Exiting...')
            exit()

    def normal_equation_estimation(self, x: np.ndarray, y: np.ndarray):
        xT = x.T
        xTx = np.dot(xT, x)
        xTx_inv = np.linalg.inv(xTx)
        xTy = np.dot(xT, y)

        betas = np.dot(xTx_inv, xTy)
        return betas