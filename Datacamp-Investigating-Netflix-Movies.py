# Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.

# Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills 
# and dive into the entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV file 
# containing Netflix data. They believe that the average duration of movies has been declining. Using your friends initial research, you'll delve 
# into the Netflix data to see if you can determine whether movie lengths are actually getting shorter and explain some of the contributing factors, if any.

# Load required libraries
import numpy as np
import pandas as pd
import matplotlib as plt

# load csv file and store as netflix_df
netflix_df = pd.read_csv("netflix_data.csv")

# check if correct dataframe is loaded in 
netflix_df.head(5)

# Filter netflix_df to remove tv shows and store as netflix_subset
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

# Inspect netflix_subset
netflix_subset.head(3)

# Create new dataframe called netflix movies, with columns "title", "country", "genre", "release_year", and "duration"
netflix_movies = netflix_subset.drop(columns = ["show_id", "type", "director", "cast", "date_added", "description"])

# inspect netflix_movies dataframe
netflix_movies.head(3)

# Filter netflix_movies that are strictly shorter than 60minutes, and save as short movies.
# Inspect possible contributing factors
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Inspect short_movies dataframe
short_movies.head(3)

# Create visualization based on release_year  
plt.hist("release_year", data = short_movies)
plt.xticks(rotation=45, ha='right')
plt.show()
plt.clf

# Create visualization based on release_year  
plt.hist("genre", data = short_movies)
plt.xticks(rotation=45, ha='right')
plt.show()
plt.clf()

# Using loop and if/elif statements, iterate through the rows of netflix_movies and assign colors of your choice to four genre groups ("Children", "Documentaries", "Stand-Up", and "Other" for everything else). Save the results in a colors list. 

# Create pandas dataframe to access to iterate over rows
netflix_pddf = pd.DataFrame(netflix_movies, columns = ["show_id", "type", "title", "director", "cast", "country", "date_added", "release_year", "duration", "description", "genre"])

# Create an empty list to store the assigned colors
colors = []  

# create loop with if/elif statements
for i, row in netflix_pddf.iterrows():
    if row['genre'] == "Children":
        colors.append("pink")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("yellow")
    else:
        colors.append("grey")

# Add a new column 'color' to the DataFrame with the assigned colors
netflix_pddf['color'] = colors

print(netflix_pddf)

# Initialize a matplotlib figure object called fig and create a scatter plot for movie duration by release year using the colors list to color the points and using the labels "Release year" for the x-axis, "Duration (min)" for the y-axis, and the title "Movie Duration by Year of Release".
fig = plt.figure()

plt.scatter(x = "release_year", y ="duration", data = netflix_pddf, c = colors, alpha = 0.5)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")

# After inspecting the plot, answer the question "Are we certain that movies are getting shorter?" by assigning either "yes" or "no" to the variable answer 
answer = "no"