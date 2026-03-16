import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
#load dataset

iris=load_iris()
X=iris.data
y=iris.target
df=pd.DataFrame(X,columns=iris.feature_names)
df["species"]=iris.target
print(df.head())
print("Features Name : ",iris.feature_names)
print("Target data : ",iris.target)
print("Target Names: ",iris.target_names)
#print("X---------------------->",X)
#split data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3, random_state=42)
#create model
model =LogisticRegression(max_iter=200)
#train model
model.fit(X_train,y_train)
#make prediction
y_pred=model.predict(X_test)
#confusion matrix
cm=confusion_matrix(y_test,y_pred)

#evolution
print("accuracy:",accuracy_score(y_test,y_pred))
print("confusion matrix:\n",confusion_matrix(y_test,y_pred))
print("classification report:\n",classification_report(y_test,y_pred))
# comparison of score on train part vs test part 
print("Train Score:", model.score(X_train, y_train)) 
print("Test Score:", model.score(X_test, y_test))
# Import libraries 
import pandas as pd 
import numpy as np 
from sklearn.datasets import load_diabetes 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_absolute_error, mean_squared_error, 
r2_score 
from sklearn.model_selection import cross_val_score 
# Load dataset 
diabetes = load_diabetes() 
X = diabetes.data 
y = diabetes.target 
df=pd.DataFrame(X,columns=diabetes.feature_names) 
print(df.head()) 
# Split data 
X_train, X_test, y_train, y_test = train_test_split( 
X, y, test_size=0.3, random_state=42 
)
# Create model 
model = LinearRegression() 
# Train model 
model.fit(X_train, y_train) 
# Predictions 
y_pred = model.predict(X_test) 
# Evaluation 
mae = mean_absolute_error(y_test, y_pred) 
mse = mean_squared_error(y_test, y_pred) 
rmse = np.sqrt(mse) 
r2 = r2_score(y_test, y_pred) 
print("MAE:", mae) 
print("MSE:", mse) 
print("RMSE:", rmse) 
print("R2 Score:", r2) 
scores = cross_val_score(model, X, y, cv=5) 
print("Cross Validation Score:", scores.mean())

