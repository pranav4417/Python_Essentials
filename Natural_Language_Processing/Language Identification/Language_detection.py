#!pip install langdetect
"""
Author: Pranav Kandakurthi  
Copyright (c) 2025 Pranav Kandakurthi  
Description: This script trains a Naïve Bayes model for language identification using TF-IDF features.  
Dependencies:- langdetect (load it using !pip install langdetect)
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load training data
train_df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Natural_Language_Processing/data/trainingData.tsv", sep="\t", header=None, names=["Text", "Language"])

# Load validation (or) testing data
val_df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Natural_Language_Processing/data/validationData.tsv", sep="\t", header=None, names=["Text", "Actual_Language"])

# Train a Naïve Bayes model with TF-IDF features
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train_df["Text"], train_df["Language"])

# Predict on validation data
val_df["Predicted_Language"] = model.predict(val_df["Text"])

# Save results
val_df[["Text", "Predicted_Language"]].to_csv("output.tsv", sep="\t", index=False)

print("Predictions saved to output.tsv")
