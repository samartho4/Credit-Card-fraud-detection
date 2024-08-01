# Part 1: Loading packages and reading data
credit_card_fraud_detection_part1 = """
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

from sklearn.model_selection import train_test_split
import os

pd.set_option('display.max_columns', 100)

# Set random seed for reproducibility
RANDOM_STATE = 2018

# Specify paths
IS_LOCAL = False

if IS_LOCAL:
    PATH = "../input/credit-card-fraud-detection"
else:
    PATH = "../input"
print(os.listdir(PATH))

# Read the data
data_df = pd.read_csv(PATH + "/creditcard.csv")

# Check the data
print("Credit Card Fraud Detection data -  rows:", data_df.shape[0], " columns:", data_df.shape[1])

# Glimpse the data
print(data_df.head())

# Describe the data
print(data_df.describe())

# Check missing data
total = data_df.isnull().sum().sort_values(ascending=False)
percent = (data_df.isnull().sum() / data_df.isnull().count() * 100).sort_values(ascending=False)
pd.concat([total, percent], axis=1, keys=['Total', 'Percent']).transpose()
"""
