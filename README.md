# Project Proposal: Genre-Based Sentiment Analysis in Movie Reviews

This project is a DSA210 term project aimed at analyzing **Genre-Based Sentiment Analysis** in movie reviews.

---

## Motivation
Movies are a significant part of our culture, and understanding how audiences perceive them across genres can provide valuable insights into changing tastes, societal trends, and the impact of different filmmaking styles. This project aims to explore the following key aspect of movie reviews:

1. **Genre-Based Sentiment Analysis**: Are there significant differences in sentiment across movie genres? Do certain genres consistently receive more polarized or positive reviews?

By analyzing these aspects, we can uncover patterns in audience preferences, the impact of genre on reception, and how the film industry has adapted to changing viewer expectations.

---

## Data Source
The primary data for this project will be sourced from publicly available datasets:

### Movie Reviews
- **Source**: IMDb, Rotten Tomatoes, or Kaggle datasets (e.g., IMDb Movie Reviews or Rotten Tomatoes Movie Reviews).
- **Collection**: Downloading pre-existing datasets. Metadata such as genre, box office earnings, and director information will be added from IMDb or The Movie Database.

### Enhancement with Additional Datasets
- **Box Office Earnings**: To explore the relationship between sentiment and financial success.
- **Awards Data**: To analyze whether award-winning movies receive more positive reviews.
- **Social Media Reactions**: Social media platforms (Reddit, etc.) for audience reactions to movies.

---

## Data Analysis

### 1. Data Collection and Cleaning
- Collect movie reviews and metadata from IMDb, Rotten Tomatoes, or Kaggle.
- Clean the data by handling missing values, removing duplicates, and standardizing formats.
- Enhance the dataset with additional features such as box office earnings, awards, and genre labels.

### 2. Feature Engineering
- **Sentiment Scores**: Use models to generate sentiment scores (positive, negative, neutral) for each review.
- **Genre-Based Features**: Encode genres as categorical variables for comparison.
- **Box Office Normalization**: Normalize box office earnings for inflation to ensure fair comparisons across years.

### 3. Sentiment Analysis
- **Sentiment Classification**: Use models to classify reviews as positive, negative, or neutral based on their text.
- **Genre-Based Sentiment Analysis**: Analyze how sentiment varies across different genres.
- **Model Evaluation**: Check the accuracy of sentiment classification using labeled data to ensure reliable results.

### 4. Visualization
- Use bar charts, box plots, and heatmaps to compare sentiment across genres.
- Visualize relationships between sentiment and box office earnings or awards within each genre.

---

## Hypothesis
There are significant differences in sentiment scores between different movie genres.

---

## Findings
The project aims to uncover the following insights:

### Genre-Based Sentiment Analysis
- Which genres receive the most positive or negative reviews?
- Are certain genres more polarizing (e.g., horror, comedy)?
- How do specific genres align with broader cultural or societal changes?

### Additional Insights
- Is there a correlation between box office earnings and sentiment scores within each genre?
- Do award-winning movies within each genre receive more positive reviews?

---

## Limitations and Future Work

### Limitations
- The accuracy of sentiment analysis depends on the quality of the NLP model and the dataset.
- Data availability for certain genres may be limited.

### Future Work
- Incorporate additional data sources, such as social media reactions or critic reviews, to enrich the analysis.
- Explore the impact of external factors (e.g., box office performance, awards) on sentiment within each genre.

---


## Project Structure

1. **Data Collection and Preprocessing**:
   - Data is gathered from IMDb and Rotten Tomatoes datasets and preprocessed to ensure clean data for analysis.

2. **Exploratory Data Analysis (EDA)**:
   - Perform initial exploratory analysis and visualize genre distribution, ratings, and correlations.

3. **Sentiment and Rating Analysis**:
   - The project analyzes sentiment across different genres, using statistical methods such as permutation tests.

4. **Statistical Hypothesis Testing**:
   - Hypothesis testing using randomization tests to compare average ratings for movies with and without specific genres.

5. **Data Visualizations**:
   - Visualizations of statistical tests, average ratings, and genre distributions.
