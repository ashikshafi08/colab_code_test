import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_regression


def make_data():
    X , y = make_regression(n_samples= 1000 , 
                            n_features= 10 , 
                            n_targets= 1) 
    return X , y


