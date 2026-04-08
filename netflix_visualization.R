library(ggplot2)
library(dplyr)
library(readr)
library(stringr)
library(tidyr)

# Load data
netflix <- read_csv("netflix_data.csv")

# Split genres and count
genre_count <- netflix %>%
  separate_rows(listed_in, sep = ",") %>%
  mutate(listed_in = str_trim(listed_in)) %>%
  count(listed_in, sort = TRUE) %>%
  slice_head(n = 10)

# Plot
ggplot(genre_count, aes(x = reorder(listed_in, n), y = n)) +
  geom_col() +
  coord_flip() +
  labs(
    title = "Top 10 Most Watched Genres on Netflix",
    x = "Genre",
    y = "Count"
  )

# Save plot
ggsave(
  "most_watched_genres_R.png",
  width = 8,
  height = 5,
  dpi = 300
)
