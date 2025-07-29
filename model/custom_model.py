import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class CustomLogisticModel:
    def __init__(self, w, b, mean=None, std=None):
        self.w = w
        self.b = b
        self.mean = mean
        self.std = std

    def scale(self, X):
        if self.mean is not None and self.std is not None:
            return (X - self.mean) / self.std
        return X
    
    def predict_proba(self, X):
        X = self.scale(X)
        z = np.dot(X, self.w) + self.b
        return 1 / (1 + np.exp(-z))

    def predict(self, X):
        X = self.scale(X)
        z = np.dot(X, self.w) + self.b
        return (1 / (1 + np.exp(-z)) >= 0.5).astype(int)

