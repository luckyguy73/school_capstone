import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import eli5
import warnings


warnings.filterwarnings('ignore')
# print('hello')

df = pd.read_csv('heart.csv')

X = df.drop(columns=['target'])
y = df.target
size = df['sex'].value_counts()
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=1, test_size=.4)
forest_model = RandomForestClassifier(n_estimators=100, max_depth=5, max_leaf_nodes=16, n_jobs=-1, random_state=10)
rf_model = forest_model.fit(train_X, train_y)


# def get_rf_prediction(patient_list, max_leaf_nodes=16):
#     pred_val = model.predict(patient_list)
#     mae = mean_absolute_error(test_y, pred_val)
#     return mae


# X = df.drop(['target'], axis=1)
# # X = df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang',
# #         'oldpeak', 'slope', 'ca', 'thal']]
# y = df.target
# train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.1, random_state=5)
# tree_model = DecisionTreeRegressor(random_state=1)
# tree_model.fit(train_X, train_y)
# predicted = tree_model.predict(test_X)
# mae = mean_absolute_error(test_y, predicted)
# best = sys.maxsize
# nodes = 1


# def get_mae_rf(max_leaf_nodes, train_X, val_X, train_y, val_y):
#     model = RandomForestRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
#     model.fit(train_X, train_y)
#     pred_val = model.predict(val_X)
#     mae = mean_absolute_error(val_y, pred_val)
#     return mae
#
#
# best = sys.maxsize
# nodes = 1
# for m in range(2, 5000):
#     mae = get_mae_rf(m, train_X, test_X, train_y, test_y)
#     if mae < best:
#         best = mae
#         nodes = m
#
# print(f'Best RandomForest mean error is {best}, by using {nodes} leaf nodes')
