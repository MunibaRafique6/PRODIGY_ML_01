# -*- coding: utf-8 -*-
"""Task-01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BKhoBAi-V66-AQ3LoI79NqeAxrGUH6zU
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

X = train_data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = train_data['SalePrice']

numeric_data = test_data.select_dtypes(include=np.number)
test_data.fillna(numeric_data.mean(), inplace=True)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_val)

mae = mean_absolute_error(y_val, y_pred)
rmse = np.sqrt(mean_squared_error(y_val, y_pred))
r2 = r2_score(y_val, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"RMSE: {rmse}")
print(f"R-squared: {r2}")

X_test = test_data[['GrLivArea', 'BedroomAbvGr', 'FullBath']].copy()
X_test.fillna(X_test.mean(), inplace=True)

test_preds = model.predict(X_test)

submission = pd.DataFrame({
    'Id': test_data['Id'],
    'SalePrice': test_preds
})
submission.to_csv('submission.csv', index=False)
print(submission.head())

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.figure(figsize=(10, 8))

numeric_data = train_data.select_dtypes(include=['number'])
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')

plt.show()