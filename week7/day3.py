
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y=(steps>= 10000).astype(int)
#sleep, water, bench

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X_train, y_train)

#Single predictions
single_day = np.array([[8.0,8,84]])  
pred = clf.predict(single_day)[0]
labels= "Goal reached" if pred ==1 else "Below"
print(f" Single predictions: {labels}")

#Batch predictons
new_days = np.array([
    [8.0, 8, 84],
    [6.0, 6, 74],
    [9.0, 9, 84],
    [7.0, 7, 82],
    [7.5, 6, 79],
])

preds = clf.predict(new_days)
print("\n Batch predictions:")
for inputs, pred in zip(new_days, preds):

    print(inputs, pred)


#2 Probability

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y=(steps>=10000).astype(int)

X_train, X_test, y_train,y_test= train_test_split(X,y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=20, random_state = 42)
clf.fit(X_train, y_train)

new_days = np.array([[8.0,8,84],[6.0,5,78],[9.0,9,87],[7.0,7,82]])
probas = clf.predict_proba(new_days)

print("Predictions with confidence:")
for inputs, proba in zip(new_days, probas):
    prob_hit = proba[1]
    label = "Goal hit" if prob_hit>= 0.5 else "Below Goal"
    confidence = max(proba) *100
    print(f" {inputs} {label} {confidence}")



    #Prediction function in a Diary Farm
    #a cow's daily feed and lactation day count, then returns whether her yield is above the 15-litre target for the day.

# Training data: [feed_kg_per_day, lactation_day]
# Label: 1 = above 15L that day, 0 = below

import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([
    [6.5, 30],
    [7.0, 45],
    [5.5, 20],
    [7.5, 60],
    [6.0, 25],
    [8.0, 75],
    [5.0, 15],
    [7.2, 50],
    [6.8, 40],
    [7.8, 70],
    [5.8, 22],
    [7.3, 55],
    [6.2, 28],
    [8.1, 80],
    [5.3, 18],
    [7.1, 48],
    [6.6, 35],
    [7.6, 65],
    [5.7, 21],
    [7.9, 72],
])
y = np.array([1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1])

clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X,y)

def predict_cows_yield(feed_kg, lactation_day):
    inputs = np.array([[feed_kg, lactation_day]])
    pred = clf.predict(inputs)[0]
    proba = clf.predict_proba(inputs)[0]
    confidence = max(proba) * 100
    status = "Above 15L" if pred==1 else "Below target"
    return status, round(confidence,1)

cows = [
    ("Cow 1 (Kamau farm)", 7.2, 50),
    ("Cow 2 (Wanjiku farm)", 5.5, 20),
    ("Cow 3 (Mwangi farm)", 7.8, 70),
]

for name, feed, days in cows:
    status, confidence = predict_cows_yield(feed, days)
    print(f"{name}: {status} -{confidence}%")




    import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def get_coaching_methods(sleep, water, bench, hit_goal, confidence):
    prompt= (f" Athlete data: sleep{sleep}h, water{water}g, bench{bench}kg"
            f" Goal predictions: {'HIT' if hit_goal else 'MISS'} ({confidence:.0%} confidence)."
            "Give a 2-sentence coaching response. be direct and specific.")
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
         {"role": "system",
          "content": ("You are an SMP performance coach"
             "You give direct, data driven coaching feedback"
             "No filer, Two sentences maximum")},
          {"role": "user", "content": prompt}
      ]
  )
    return response.choices[0].message.content
