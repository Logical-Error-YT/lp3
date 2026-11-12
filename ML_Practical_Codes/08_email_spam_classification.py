# Email Spam Detection (binary classification)
# Dataset CSV should contain text and label columns (edit names if needed).
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("spam.csv", encoding="latin-1")
# Common SMS Spam Collection columns: v1 = label, v2 = message
df = df.rename(columns={"v1": "label", "v2": "message"})
df = df[["label", "message"]].dropna()
df["label"] = df["label"].map({"ham": "NotSpam", "spam": "Spam"}).fillna(df["label"])

X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label"], test_size=0.2, random_state=42, stratify=df["label"])

model = Pipeline([("tfidf", TfidfVectorizer()), ("nb", MultinomialNB())])
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

msg = input("\nEnter an email/message: ")
print("Prediction:", model.predict([msg])[0])
