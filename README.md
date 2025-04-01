# Project Proposal: Sentiment Trends Over Time and Genre-Based Sentiment Analysis in Movie Reviews

This project is a DSA210 term project aimed at analyzing **Sentiment Trends Over Time** and **Genre-Based Sentiment Analysis** in movie reviews.

---

## Motivation
Movies are a significant part of our culture, and understanding how audiences perceive them over time and across genres can provide valuable insights into changing tastes, societal trends, and the impact of different filmmaking styles. This project aims to explore two key aspects of movie reviews:

1. **Sentiment Trends Over Time**: How have movie review sentiments evolved over the years? Are newer movies receiving more positive or negative reviews compared to older ones?
2. **Genre-Based Sentiment Analysis**: Are there significant differences in sentiment across movie genres? Do certain genres consistently receive more polarized or positive reviews?

By analyzing these aspects, we can uncover patterns in audience preferences, the impact of genre on reception, and how the film industry has adapted to changing viewer expectations.

---

## Data Source
The primary data for this project will be sourced from publicly available datasets:

### Movie Reviews
- **Source**: IMDb, Rotten Tomatoes, or Kaggle datasets (e.g., IMDb Movie Reviews or Rotten Tomatoes Movie Reviews).
- **Collection**: Downloading pre-existing datasets. Metadata such as genre, release year, box office earnings, and director information will be added from IMDb or The Movie Database.

### Enhancement with Additional Datasets
- **Box Office Earnings**: To explore the relationship between sentiment and financial success.
- **Awards Data**: To analyze whether award-winning movies receive more positive reviews.
- **Social Media Reactions**: Social media platforms (Reddit etc.) for audience reactions to movies.

---

## Data Analysis

### 1. Data Collection and Cleaning
- Collect movie reviews and metadata from IMDb, Rotten Tomatoes, or Kaggle.
- Clean the data by handling missing values, removing duplicates, and standardizing formats.
- Enhance the dataset with additional features such as box office earnings, awards, and genre labels.

### 2. Feature Engineering
- **Sentiment Scores**: Use models to generate sentiment scores (positive, negative, neutral) for each review.
- **Time-Based Features**: Create features such as release year and decade to analyze trends over time.
- **Genre-Based Features**: Encode genres as categorical variables for comparison.
- **Box Office Normalization**: Normalize box office earnings for inflation to ensure fair comparisons across years.

### 3. Sentiment Analysis
- **Sentiment Classification**: Use models to classify reviews as positive, negative, or neutral based on their text.
- **Trend Analysis**: Analyze how sentiment scores change over time and across different genres.
- **Model Evaluation**: Check the accuracy of sentiment classification using labeled data to ensure reliable results.

### 4. Visualization
- Create time series plots to show sentiment trends over time.
- Use bar charts, box plots, and heatmaps to compare sentiment across genres.
- Visualize relationships between sentiment and box office earnings or awards.

---

## Findings
The project aims to uncover the following insights:

### Sentiment Trends Over Time
- Are newer movies receiving more positive or negative reviews compared to older ones?
- Are there specific years or decades where sentiment shifted significantly?

### Genre-Based Sentiment Analysis
- Which genres receive the most positive or negative reviews?
- Are certain genres more polarizing (e.g., horror, comedy)?
- Do genre-specific trends align with broader cultural or societal changes?

### Additional Insights
- Is there a correlation between box office earnings and sentiment scores?
- Do award-winning movies receive more positive reviews?

---

## Limitations and Future Work

### Limitations
- The accuracy of sentiment analysis depends on the quality of the NLP model and the dataset.
- Data availability for older movies may be limited.

### Future Work
- Incorporate additional data sources, such as social media reactions or critic reviews, to enrich the analysis.
- Explore the impact of external factors (e.g., box office performance, awards) on sentiment.

----
## Project Files:
- `main.py` → Runs the entire analysis.
- `data_collection.py` → Collects movie reviews.
- `sentiment_analysis.py` → Assigns sentiment scores.
- `eda.py` → Explores and visualizes data.
- `hypothesis_testing.py` → Performs statistical hypothesis testing.

## Steps in the Analysis:
1. **Data Collection** → Scrape or load movie reviews.
2. **Sentiment Analysis** → Apply sentiment scoring.
3. **EDA (Exploratory Data Analysis)** → Generate graphs & insights.
4. **Hypothesis Testing** → Test for statistical significance.
