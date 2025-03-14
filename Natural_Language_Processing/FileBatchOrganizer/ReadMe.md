# 📌 Document Similarity Finder

## 📢 Overview
This script calculates the **cosine similarity** between a set of **20 documents** represented as a **bag of words**. It identifies the most similar document for each document in the corpus.

## 🛠 Features
✅ Automatically scans and processes all document columns.  
✅ Computes cosine similarity between all document pairs.  
✅ Identifies the most similar document for each input document.  
✅ Works dynamically for any number of documents.  

## 📂 Dataset Format
- The dataset should be an **Excel file (.xlsx)** containing:
  - **First column**: Words (features).
  - **Remaining columns**: Document term frequencies (D1, D2, ..., D20).
  
Example:
| Word      | D1 | D2 | D3 |
|-----------|----|----|----|
| grave     |  1 |  0 |  0 |
| us        |  4 |  0 |  0 |
| fit       |  0 |  1 |  0 |
| remembered|  2 |  0 |  2 |

## 🚀 Installation & Usage
### 1️⃣ **Install Required Libraries**
Ensure you have Python installed. Install dependencies using:

```bash
pip install pandas scikit-learn openpyxl
```


Let me know if you need modifications! 🚀
