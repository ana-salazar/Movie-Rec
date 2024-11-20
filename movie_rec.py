import pandas as pd

class Movie:
    """
    class representing a movie by its attributes
    
    Attributes:
    rank(int): the rank of the movie in the movie database
    name(str): name of the movie
    year(int): year movie was released
    rating(float): the IMDB rating (rating of the movie out of 9)
    genre(str): the genre of the movie
    certificate(str): the movie rating (PG-13, PG, R, Approved, Not Rated, G, Passed, Unrated, X, 13+, TV-MA)
    run_time(int): the runtime of the movie
    tagline(str): the movies tagline
     
    
    """
    
    def __init__(self, rank, name, year, rating, genre, certificate, run_time, tagline):
        self.rank = rank
        self.name = name
        self.year = year
        self.rating = rating
        self.genre = genre
        self.certificate = certificate
        self.run_time = run_time
        self.tagline = tagline
        
        
# load the dataset
file_path = '/mnt/data/IMDB Top 250 Movies.csv'
movies_df = pd.read_csv(file_path)

# convert the runtime from string format (ex/ '2h 22m') to minutes
def convert_runtime(runtime):
    hours, minutes = 0, 0
    if 'h' in runtime:
        hours = int(runtime.split('h')[0])
        if 'm' in runtime:
            minutes = int(runtime.split('h')[1].strip('m'))
    return hours * 60 + minutes

# create Movie instances from the DataFrame
movie_list = []
for _, row in movies_df.iterrows():
    movie = Movie(
        rank=row['rank'],
        name=row['name'],
        year=row['year'],
        rating=row['rating'],
        genre=row['genre'],
        certificate=row['certificate'],
        run_time=row['runtime_minutes'],
        tagline=row['tagline']
    )
    movie_list.append(movie)

# apply the conversion
movies_df['runtime_minutes'] = movies_df['run_time'].apply(convert_runtime)

# function to recommend movies based on user input
def recommend_movies(genre=None, min_rating=0, max_runtime=999, certificate=None):
    if genre:
        genre_filter = movies_df['genre'].str.contains(genre, case=False, na=False)
    else:
        genre_filter = True
