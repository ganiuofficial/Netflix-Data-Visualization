import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Netflix_shows_movies/netflix_data.csv")

print(df.shape)
print(df.columns)

# Clean missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# Exploring the data
print(df.describe(include='all'))

print(df['type'].value_counts())

print(df['rating'].value_counts().head(10))

# Prepare genres
genres = df['listed_in'].str.split(',').explode().str.strip()

# Plotting most watching genre
top_genres = genres.value_counts().head(10).index.tolist()

# Filter genres to top 10 only
genres_top10 = genres[genres.isin(top_genres)]

plt.figure(figsize=(12, 6))
sns.countplot(
    y=genres_top10,
    order=top_genres
)
plt.title("Most Watched Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.grid(True)
plt.savefig("most_watched_genres.png")
plt.show()

# Ratings distribution plot
plt.figure(figsize=(10, 5))

# Only include ratings that exist in the data
rating_order = df['rating'].value_counts().index.tolist()

sns.countplot(
    x='rating',
    data=df,
    order=rating_order
)

plt.title("Ratings Distribution on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.grid(True)
plt.savefig("ratings_distribution.png")
plt.show()
