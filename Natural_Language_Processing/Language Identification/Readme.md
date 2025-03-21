# Language Detection Script

## Description
This script trains a Naïve Bayes model for language identification using TF-IDF features. It predicts the language of given text based on a trained model.

## Dependencies
- `langdetect`: Install using `pip install langdetect`
- `pandas`: Install using `pip install pandas`
- `scikit-learn`: Install using `pip install scikit-learn`

## Usage
1. Ensure you have the required dependencies installed.
2. Place your training and validation data in the specified paths.
3. Run the script using Python:
   ```bash
   python lang_detect.py
   ```

## Data
- The training data should be in a tab-separated values (TSV) format with two columns: Text and Language.
- The validation data should also be in TSV format with two columns: Text and Actual_Language.

## Output
The script will save the predictions to `output.tsv`, which contains the original text and the predicted language.

## Author
Pranav Kandakurthi
