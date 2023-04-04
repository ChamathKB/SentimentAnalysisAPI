import pytest
import pickle
import numpy as np
from model import NLPModel

model = NLPModel()

model_path = 'lib/models/SentimentClassifier.pkl'

with open(model_path, 'rb') as f:
    model.clf = pickle.load(f)

vec_path = 'lib/models/TFIDFVectorizer.pkl'

with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)

def test_predict():
    user_query = "that movie was boring"

    uq_vectorize = model.vectorizer_transform(np.array([user_query]))
    prediction = model.predict(uq_vectorize)
    pred_proba = model.predict_proba(uq_vectorize)

    assert prediction == 0