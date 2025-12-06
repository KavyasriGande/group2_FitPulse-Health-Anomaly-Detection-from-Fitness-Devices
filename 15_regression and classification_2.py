import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Create age range
ages = np.arange(1, 81) # Age 1 to 80

heights = []

for age in ages:
    if age <= 30:
        # Height increases linearly with some noise
        height = 50 + age * 2 + np.random.normal(0, 1)
    elif 30 < age < 55:
        # Height stays stable
        height = 110 + np.random.normal(0, 1)
    else:
        # Height decreases after 55
        height = 110 - (age - 55) * 1.5 + np.random.normal(0, 1)

    heights.append(height)

# Create DataFrame
df = pd.DataFrame({
    'age': ages,
    'height': heights
})

print(df.head())
print(df.tail())

#features->x and Target->y
x=df[['age']]
y=df[['height']]

#spilt data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
model=LinearRegression()
model.fit(x_train,y_train)

#predict
pred=model.predict(x_test)

print("Predicted height ",pred)

print("MSE",mean_squared_error(y_test,pred))


# (Optional) Train-test split for ML
# X_train, X_test, y_train, y_test = train_test_split(df[['age']], df['height'], test_size=0.2, random_state=42)