# train_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

# Sample training data (replace with IMDb or Twitter dataset for more realism)
texts = [
    "I love this movie", "This movie is terrible",
    "Absolutely fantastic!", "Not good",
    "Best experience ever", "Worst thing I have seen",
    "I am so happy", "I hate this"
]
labels = ["positive", "negative", "positive", "negative",
          "positive", "negative", "positive", "negative"]

# Create a pipeline: Vectorizer + Classifier
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(texts, labels)

# Save the trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")