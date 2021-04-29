import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Read in IMDB movie metadata CSV file. 
df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')

# fig = plt.figure()
# x = np.arange(6)
# y = np.arange(6)
# plt.plot(x, y)
# plt.xlabel("Number of donuts eaten")
# plt.ylabel("Miles unicycled")
# plt.title("Correlation does not equal Causation")
# fig.savefig("a_plot.png")

# initializing matplotlib figure
fig = plt.figure(figsize=(11,8))

# total number of facebook likes for each leading actor
actor = df.groupby(['actor_1_name'])['actor_1_facebook_likes'].sum()
actor = actor.sort_values(ascending=False)
print(actor.head(10))
actor[:10].plot(kind="barh")
plt.xlabel("Facebook Likes")
plt.title("10 Actors with Most Facebook Likes")
fig.savefig('actor.png')

fig = plt.figure()

# number of movies made by each director
num_movies = df['director_name'].value_counts()[:15]
print(num_movies)
num_movies.plot(kind="barh")
fig.savefig('num_movies.png')