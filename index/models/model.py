import numpy as np
import os

from keras.utils import np_utils
from keras.datasets import mnist
from keras.layers import Activation, Dense
from keras.models import Sequential
from keras.models import load_model
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
model = load_model("index\models\my_model.h5")

def predict_number(m):
    result = model.predict(m)
    return result
