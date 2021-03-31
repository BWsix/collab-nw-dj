import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.datasets import mnist
from keras.layers import Activation, Dense
from keras.models import Sequential


model = load_model("my_model.h5")

def predict_number(m):
    result = model.predict(m)
    return result