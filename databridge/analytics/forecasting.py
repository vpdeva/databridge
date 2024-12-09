
from sklearn.linear_model import LinearRegression
import numpy as np

def time_series_forecasting(data, look_back=3):
    """
    Basic time-series forecasting using linear regression.
    """
    X = np.array([data[i:i + look_back] for i in range(len(data) - look_back)])
    y = np.array(data[look_back:])
    model = LinearRegression().fit(X, y)
    return model.predict(X)
            