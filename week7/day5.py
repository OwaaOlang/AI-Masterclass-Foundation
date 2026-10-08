

#1.Teain the classifier
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 28-day SMP training data
# Features: [sleep_hr, water_glasses, bench_kg]

X = np.array([
    [6.5, 6, 80], [7.2, 8, 85], [5.8, 5, 75], [8.0, 10, 90],
    [7.5, 9, 88], [6.0, 6, 78], [7.8, 8, 86], [8.2, 10, 92],
    [5.5, 4, 70], [7.0, 7, 82], [6.8, 8, 84], [8.5, 11, 95],
    [7.3, 9, 89], [6.2, 6, 76], [7.9, 10, 91], [5.9, 5, 73],
    [8.1, 11, 93], [7.4, 8, 87], [6.7, 7, 83], [8.3, 10, 94],
    [5.6, 4, 71], [7.1, 8, 85], [8.0, 9, 90], [6.4, 6, 77],
    [7.6, 9, 88], [8.4, 11, 96], [6.3, 7, 79], [7.7, 10, 91]
])

# Labels: 1 = hit 10,000 steps, 0 = did not
y = np.array([0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1])

#split 80|20
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#Train
clf= RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

#Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)

print(f"Training rows: {len(X_train)}")
print(f" Testing rows: {len(X_test)}")
print(f" Accuracy on test: {accuracy:.0%}")

#feature importance
features = ["sleep_hr", "water_glasses", "bench_kg"]
importances = clf.feature_importances_
print()

print("Feature importances:")
for name, imp in sorted (zip(features, importances)):
    print(f" {name}  {imp}")



2. # Build the coaching layer
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    prompt = (f"Athlete data: sleep {sleep}h, water {water} glasses, "
              f"bench {bench}kg. "
              f"Goal prediction: {'HIT' if hit_goal else 'MISS'} ({confidence:.0%} confidence). "
              "Give a 2-sentence coaching response. Be direct and specific.")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": ("You are an SMP performance coach. "
                          "You give direct, data-driven coaching feedback. "
                          "No filler. Two sentences maximum.")},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


    #3. simulated coaching layer

# The response structure mirrors the OpenAI API object

class SimulatedMessage:
    def __init__(self, content):
        self.content = content

class SimulatedChoice:
    def __init__(self, content):
        self.message = SimulatedMessage(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [SimulatedChoice(content)]

    # --- Coaching templates ---
COACHING_TEMPLATES = {
    (True, True, True):  ("Strong inputs, strong output. Baseline is locked in.",
                          "Keep this pattern consistent."),
    (True, True, False): ("Hit the goal despite low water. Sleep is the primary driver.",
                          "Close the hydration gap tomorrow."),

}

def analyse_day(sleep_hr, water_glasses, bench_kg):
    features = np.array([[sleep_hr, water_glasses, bench_kg]])
    prediction = clf.predict(features)[0]
    proba = clf.predict_proba(features)[0]
    confidence = proba[prediction]
    return {
        "label":         day_label or "Day",
        "sleep_hr":      sleep_hr,
        "water_glasses": water_glasses,
        "bench_kg":      bench_kg,
        "hit_goal":      bool(prediction),
        "confidence":    confidence,
        "coaching":      coaching,
    }

# Test on three new days
new_days = [
    (8.0, 10, 92),   # strong day
    (5.5,  4, 70),   # weak day
    (7.2,  7, 84),   # borderline day
]

for sleep, water, bench in new_days:
    result = analyse_day(sleep, water, bench)
    outcome = "HIT GOAL" if result["hit_goal"] else "MISS GOAL"
    print(f" {outcome} ({result["confidence"]:.0%}) | sleep = {result["sleep_hr"]}h water={result["water_glasses"]} bench={result["bench_kg"]} | coach={result["coaching"]}")




