# Define hypothesis tests
HYPOTHESES = [
    "Sentiment scores have become more positive over time",
    "Action movies receive more negative reviews than Drama movies",
    "Oscar-winning movies have higher sentiment scores than non-winners"
]

def test_oscar_winner_hypothesis(df):
    """Test if Oscar winners have higher sentiment"""
    if 'oscar_winner' in df.columns:
        winners = df[df['oscar_winner']]['sentiment']
        others = df[~df['oscar_winner']]['sentiment']
        
        t_stat, p_value = stats.ttest_ind(winners, others)
        print(f"\nOscar Winners vs Others: p-value = {p_value:.4f}")
        if p_value < 0.05:
            print("Significant difference found")
            print(f"Winner avg: {winners.mean():.2f}, Others avg: {others.mean():.2f}")
