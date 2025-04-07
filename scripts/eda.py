import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

metadata = pd.read_csv("data/processed/movie_metadata.csv")

def run_eda():
    print(metadata.describe())
    print(metadata["genres"].value_counts())

    sns.histplot(metadata["year"], bins=20, kde=True)
    plt.title("Distribution of Movie Release Years")
    plt.savefig("outputs/release_years_hist.png")

if __name__ == "__main__":
    run_eda()
