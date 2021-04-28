import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')

print(df.head(5))
print(df.columns)

print(df['director_name'])

cols = ['movie_title', 'facenumber_in_poster']
print(df[cols])

# movies with IMDB score > 7.5

rating = df[df['imdb_score'] > 7.5]
print(rating[['movie_title','imdb_score']])

# How many movies came from each country?
country = df['country'].value_counts()
print(country.head(10))

# Which director made the most money?
df_gross = df.groupby('director_name')['gross'].sum()
df_gross = df_gross.sort_values(ascending=False)
print(df_gross.head(10))

# df_gross['num_movies'] = df.groupby(['director_name'])['movie_title'].count().squeeze()
# print(df_gross.head(10))

# How many movies were made each year?
df_movies_year = df.groupby(['title_year'])['movie_title'].count()
print(df_movies_year.head(50))

langs = df['language'].unique()
print(langs)