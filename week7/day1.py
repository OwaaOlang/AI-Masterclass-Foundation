#ML

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Data (28 days of SMP fitness log)
# Features: sleep hours, water glasses
# Label: steps taken that day

X = np.array([
    [7.5, 7], [8.0, 8], [6.5, 6], [7.0, 9], [9.0, 8], [7.5, 7], [8.0, 8],
    [6.0, 6], [8.5, 9], [7.0, 8], [7.5, 8], [9.0, 7], [7.0, 9], [7.5, 8],
    [7.0, 7], [8.0, 8], [6.5, 6], [7.5, 9], [8.0, 8], [7.0, 7], [8.5, 9],
    [7.0, 8], [7.5, 8], [6.5, 6], [8.0, 9], [9.5, 7], [7.0, 8], [8.0, 9]
])  # shape: (28, 2) - 28 days, 2 features each

y = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])  # shape: (28,) - one step count per day

print(f" Features shape: {X.shape}")
print(f" Labels shape: {y.shape}")

#2. split into train and test
X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTraining rows:  {X_train.shape[0]}")
print(f" Test rows: {X_test.shape[0]}")

#3. create and train model
model = LinearRegression()
model.fit(X_train, y_train)

#4.Evaluation
score = model.score(X_test,y_test)
print(f"\nmodel R2: {score}")
print("(1.0= perfect, 0= no better than guessing the mean)")


#Ex 2 making Predictions

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


X = np.array([[7.5,7],[8.0,8],[6.5,6],[7.0,9],[9.0,8],[7.5,7],[8.0,8],[6.0,6],[8.5,9],[7.0,8],[7.5,8],[9.0,7],[7.0,9],[7.5,8],[7.0,7],[8.0,8],[6.5,6],[7.5,9],[8.0,8],[7.0,7],[8.5,9],[7.0,8],[7.5,8],[6.5,6],[8.0,9],[9.5,7],[7.0,8],[8.0,9]])
y = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

#Predict for days not above
new_days = np.array ([
    [8.0, 8],
    [6.0, 5],
    [9.0, 9],
    [7.5, 7],
])

predictions = model.predict(new_days)
print("\nPredictions for new days:")
for i, (inputs, pred) in enumerate(zip(new_days, predictions)):
    sleep, water = inputs
    print(f"sleep={sleep}h, water={water}g predicted steps: {pred}")

#Alternatively
new_days = np.array ([[8.0, 8],[6.0, 5],[9.0, 9], [7.5, 7],]) # sleep, water
predictions = model.predict(new_days)
for (sleep, water), item in zip(new_days, predictions):
    print(f" sleep={sleep}h, water={water}g : {item:.0f} steps")


    # Example 3
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7],[8.0,8],[6.5,6],[7.0,9],[9.0,8],[7.5,7],[8.0,8],[6.0,6],[8.5,9],[7.0,8],[7.5,8],[9.0,7],[7.0,9],[7.5,8],[7.0,7],[8.0,8],[6.5,6],[7.5,9],[8.0,8],[7.0,7],[8.5,9],[7.0,8],[7.5,8],[6.5,6],[8.0,9],[9.5,7],[7.0,8],[8.0,9]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])

#convert steps count to binary labels: 1= hit goals, 0 = missed
y= (steps>= 10000).astype(int)
print("\nLabel distribution (1=hit goal, 0 = missed):")
print(f" Hit goal: {y.sum()}/28 days")
print(f" Missed: {(y==0).sum()}/ 28 days")

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size= 0.2, random_state= 42)
clf = RandomForestClassifier(n_estimators =10, random_state = 42)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("\nClassification accuracy: {accuracy:0%}")

#predict new day
new_days= np.array([[8.0,8], [6.0,5],[9.,9]])
preds = clf.predict(new_days)
labels = {1: "Goal hit", 0:"Below hit"}
print("\npredictions for new day:")
for (water, sleep), pred in zip(new_days, preds):
    print(f" sleep={sleep}h, water={water}g : {labels[pred]}")


