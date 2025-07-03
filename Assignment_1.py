import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
d1=pd.read_csv("train.csv")
d2=pd.read_csv("test.csv")
train_data=pd.DataFrame(d1)
test_data=pd.DataFrame(d2)
#print(train_data.head())

Y_train=train_data["medv"]
X_train=train_data.drop(["medv","ID"],axis=1)
#print(X_train.head())

scaler= StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test = test_data.drop(["ID"], axis=1)
X_test_scaled = scaler.transform(X_test)
#print(X_train.head())

X_scaled_df = pd.DataFrame(X_train_scaled, columns=X_train.columns)
co = X_scaled_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(co,cbar=True,square=True)
model = LinearRegression()
model.fit(X_train_scaled, Y_train)

Y_predict=model.predict(X_train_scaled)

df = pd.DataFrame({'x': Y_train, 'y': Y_predict})

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='x', y='y')
plt.show()

r2_score1=r2_score(Y_train,Y_predict)


Y_test=model.predict(X_test_scaled)

print(Y_test)









