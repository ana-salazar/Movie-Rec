class Movie:
    """
    Class representing a movie by its attributes
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
        
    def matches_filters(self, genre=None, decade=None, min_rating=None, certificate=None):
        if genre and genre.lower() not in self.genre.lower():
            return False
        if decade and (self.year // 10) * 10 != decade:
            return False
        if min_rating and self.rating < min_rating:
            return False
        if certificate and self.certificate.lower() != certificate.lower():
            return False
        return True

class MovieRecommender:
    """
    Class to handle movie recommendation logic
    """
    def __init__(self, movie_list):
        self.movies = movie_list

    def recommend_movies(self, genre=None, min_rating=0, max_runtime=999, certificate=None, sort_by=None):
        """
        Recommend movies based on filters and optionally sort the results.
        """
        recommendations = []
        for movie in self.movies:
            if (
                movie.matches_filters(genre=genre, min_rating=min_rating, certificate=certificate)
                and movie.run_time <= max_runtime
            ):
                recommendations.append(movie)
        
        if sort_by:
            recommendations = self.sort_recommendations(recommendations, sort_by)
        return recommendations

    def sort_recommendations(self, recommendations, sort_by):
        """
        Sort the recommendations by rating, runtime, or year.
        """
        if sort_by == "rating":
            return sorted(recommendations, key=lambda x: x.rating, reverse=True)
        elif sort_by == "runtime":
            return sorted(recommendations, key=lambda x: x.run_time)
        elif sort_by == "year":
            return sorted(recommendations, key=lambda x: x.year, reverse=True)
        else:
            raise ValueError(f"Invalid sort_by value: {sort_by}")

    def display_recommendations(self, recommendations, sort_by=None):
        """
        Display recommendations in a user-friendly format.
        """
        if sort_by:
            print(f"Movies sorted by: {sort_by.capitalize()}\n")
        for movie in recommendations:
            print(f"{movie.rank}. {movie.name} ({movie.year}) - {movie.rating}/10")
            print(f"   Genre: {movie.genre} | Certificate: {movie.certificate} | Runtime: {movie.run_time} mins")
            print(f"   Tagline: {movie.tagline}")
            print("-" * 50)

class MovieAnalyzer:
    """
    Class to analyze movie dataset for insights
    """
    def __init__(self, movie_list):
        self.movies = movie_list

    def genre_statistics(self):
        """
        Get statistics on movie genres.
        """
        genres = []
        for movie in self.movies:
            genres.extend(movie.genre.split(", "))
        genre_counts = Counter(genres)
        return genre_counts

    def average_rating(self):
        """
        Calculate the average rating of all movies.
        """
        total_rating = sum(movie.rating for movie in self.movies)
        return total_rating / len(self.movies)

    def yearly_trends(self):
        """
        Display trends in movie releases per year.
        """
        year_counts = Counter(movie.year for movie in self.movies)
        return dict(sorted(year_counts.items()))

def convert_runtime(runtime):
    """
    Convert the runtime from string format (e.g., '2h 22m') to minutes
    """
    hours, minutes = 0, 0
    if 'h' in runtime:
        hours = int(runtime.split('h')[0])
        if 'm' in runtime:
            minutes = int(runtime.split('h')[1].strip('m'))
    return hours * 60 + minutes

if __name__ == "__main__":
    # Load the dataset
    file_path = '/mnt/data/IMDB Top 250 Movies.csv'
    movies_df = pd.read_csv(file_path)

    # Apply runtime conversion
    movies_df['runtime_minutes'] = movies_df['run_time'].apply(convert_runtime)

    # Create Movie instances from the DataFrame
    movie_list = [
        Movie(
            rank=row['rank'],
            name=row['name'],
            year=row['year'],
            rating=row['rating'],
            genre=row['genre'],
            certificate=row['certificate'],
            run_time=row['runtime_minutes'],
            tagline=row['tagline']
        )
        for _, row in movies_df.iterrows()
    ]
