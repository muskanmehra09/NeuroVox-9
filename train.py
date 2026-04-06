import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1: Load dataset
df = pd.read_csv("features.csv")

# Step 2: Split into features (X) and labels (y)
X = df.iloc[:, :-1]   # all columns except last
y = df.iloc[:, -1]    # last column only

# Step 3: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))