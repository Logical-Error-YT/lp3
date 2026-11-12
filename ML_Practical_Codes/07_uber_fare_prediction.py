# Uber Fare Prediction: preprocessing, outliers, correlation, Linear Regression & Random Forest
# Dataset: uber.csv (change filename below if needed)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

df = pd.read_csv("uber.csv")
df = df.drop(columns=["Unnamed: 0", "key"], errors="ignore")
df = df.dropna()
df = df[(df["fare_amount"] > 0) & (df["passenger_count"].between(1, 6))]
df = df[df["pickup_longitude"].between(-180, 180) & df["dropoff_longitude"].between(-180, 180)]
df = df[df["pickup_latitude"].between(-90, 90) & df["dropoff_latitude"].between(-90, 90)]

# Outlier removal using IQR on fare_amount
Q1, Q3 = df["fare_amount"].quantile([0.25, 0.75])
IQR = Q3 - Q1
df = df[df["fare_amount"].between(Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)]

# Correlation
print("Correlation with fare_amount:\n", df.select_dtypes("number").corr()["fare_amount"].sort_values(ascending=False))
df.select_dtypes("number").corr().to_csv("correlation.csv")

# Features and target
X = df[["pickup_longitude", "pickup_latitude", "dropoff_longitude",
        "dropoff_latitude", "passenger_count"]]
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression (scale features)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
lr = LinearRegression().fit(X_train_s, y_train)
rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1).fit(X_train, y_train)

for name, model, xt in [("Linear Regression", lr, X_test_s), ("Random Forest", rf, X_test)]:
    pred = model.predict(xt)
    print(f"\n{name}")
    print("R2:", round(r2_score(y_test, pred), 4))
    print("RMSE:", round(np.sqrt(mean_squared_error(y_test, pred)), 4))
    print("MAE:", round(mean_absolute_error(y_test, pred), 4))
