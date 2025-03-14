"""
Document Similarity Finder
Author: Pranav Kandakurthi
Copyright © 2025 Pranav Kandakurthi. All rights reserved.

Description: This script calculates cosine similarity between documents 
             and finds the most similar document for each.
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

file = "/content/Data (1).xlsx"
data = pd.read_excel(file)

docs = data.iloc[:, 1:].values.T  
similarity_matrix = cosine_similarity(docs)

labels = data.columns[1:]  
similarity_df = pd.DataFrame(similarity_matrix, index=labels, columns=labels)

for doc in labels:
    others = similarity_df.loc[doc].drop(doc)  
    best_match = others.idxmax()  
    print(f"Document: {doc} → Most Similar: {best_match}\n" + "-"*30)
