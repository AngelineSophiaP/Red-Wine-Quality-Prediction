import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

print(df.isnull().sum())
df = df.drop_duplicates()
print("unique values :", df['quality'].unique())
print("count of unique values:", df['quality'].value_counts())

df['quality'] = df['quality'].apply(lambda x : 1 if x >= 6 else 0)
print("after conversion :", df['quality'].value_counts())

X = df.drop('quality', axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=4, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f" Accuracy: {acc:.2f}")

print("\n Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\n Classification Report:")
print(classification_report(y_test, y_pred))