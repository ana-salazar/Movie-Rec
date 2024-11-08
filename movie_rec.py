import pandas as pd

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

# apply the conversion
movies_df['runtime_minutes'] = movies_df['run_time'].apply(convert_runtime)

# function to recommend movies based on user input
def recommend_movies(genre=None, min_rating=0, max_runtime=999, certificate=None):
    if genre:
        genre_filter = movies_df['genre'].str.contains(genre, case=False, na=False)
    else:
        genre_filter = True
