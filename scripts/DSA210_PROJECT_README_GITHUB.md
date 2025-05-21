## **Step 1: Upload the Data to Google Colab**

## **Step 2: Load the Data**

## **Step 3: Visualize the Distribution of IMDb Average Ratings**



4. Genre-Based Analysis

5. Sentiment Analysis on Rotten Tomatoes Reviews

1. Data Transformation (Sentiment Score Extraction)

Apply VADER sentiment analysis to Rotten Tomatoes reviews:

Step-by-Step: Correlation Visualization

## **Step 3: Hypothesis Testing with Your IMDb Data**

𝐻
0
H
0
​
 : There is no difference in average ratings between movies with the target genre and those without.

𝐻
𝐴
H
A
​
 : There is a significant difference in average ratings.


3.1: Load and Merge the Data

3.2: Calculate Correlation Coefficients

Randomization Test (Permutation Test) for Genre vs Rating

Setup and Drive Mounting

Install and Import **Packages**

Load IMDb Data from Google Drive

Define the ML Task (Markdown cell)

🎯 ML Task: Predict whether a movie belongs to the "Action" genre
🧪 Target Variable: is_action (1 = Action, 0 = Not Action)
📘 Data: IMDb title and ratings metadata
✅ Goal: Build a binary classifier using IMDb ratings to identify Action-genre films


Merge Metadata and Ratings

Create a Binary Label for a Genre (e.g., Action)

Prepare Data for ML

Train/Test Split

Train Logistic Regression Model

Evaluate Performance

Summary:

✅ This project successfully predicts whether a film belongs to the "Action" genre based on IMDb metadata.

🎯 ML task: Binary classification (`is_action`)

📘 Data: IMDb basics and ratings merged on `tconst`

📈 Model: Logistic Regression

💡 Features: `averageRating`, `title_length`

🔁 Data enrichment: Added `title_length` and balanced dataset

🧪 Result: Model predicts both classes with ~53% accuracy
