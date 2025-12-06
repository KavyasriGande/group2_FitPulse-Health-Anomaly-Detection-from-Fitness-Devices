import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error
#sample dataset
data=pd.DataFrame({"area":[1000,1500,2500,6000],
                    "price":[10,15,20,50]})
 
#features->x and Target->y
x=data[['area']]
y=data[['price']]
 
#spilt data 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
model=LinearRegression()
model.fit(x_train,y_train)
 
#predict
pred=model.predict(x_test)
 
print("Predicted prices ",pred)
print("MSE",mean_squared_error(y_test,pred))