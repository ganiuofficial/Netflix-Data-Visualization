# Module 4 Assignment: Netflix Data Visualization

## Overview
This project analyzes a Netflix dataset containing shows and movies. The analysis uses Python for data cleaning, exploration, and visualization, and R for one chart as part of integration.

## Dataset
- File: netflix_data.csv
- Rows: 6,234  
- Columns: 12 (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)

## Python Instructions
1. Open netflix_analysis.py in Python 3.14+.
2. Run the script.
3. Outputs generated:
   - most_watched_genres.png → Top 10 most watched genres
   - ratings_distribution.png → Distribution of ratings

**Notes:**
- Missing values handled for director, cast, country, and rating.
- Top 10 genres plotted for readability.

## R Instructions
1. Open netflix_visualization.R in RStudio.
2. Ensure required packages are installed: ggplot2, dplyr, tidyr, etc.
3. Run the script to generate:
   - most_watched_genres_R.png → Top 10 genres chart in R
4. The chart replicates the Python genre visualization.

**Notes:** 
The R analysis reproduces the Python results by splitting the **listed_in** field into individual genres, counting occurrences, and visualizing the top 10 genres using **ggplot2**.

## Submission Files
- netflix_analysis.py → Python analysis script  
- netflix_visualization.R → R visualization script  
- netflix_data.csv → Dataset  
- most_watched_genres.png → Python plot  
- ratings_distribution.png → Python plot
- most_watched_genres_with_grid.png → Python plot  
- ratings_distribution_with_grid.png → Python plot  
- most_watched_genres_R.png → R plot 
- README.md → Instructions and overview
