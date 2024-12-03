import sqlite3
import csv

class MovieDatabase:
    def __init__(self, movie_csv= 'IMDB Top 250 Movies.csv', db = 'topmovies.db'):
        self.movie_csv = movie_csv
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.movie_table()
        self.add_movies() #add the top movies  
    def movie_table(self):
        self.cursor.execute( 
        """
        CREATE TABLE movies (
        rank INTEGER PRIMARY KEY, name TEXT, year INTEGER, 
        rating REAL, genre TEXT, certificate TEXT, run_time TEXT, tagline TEXT,
        budget INTEGER, box_office INTEGER, casts TEXT, directors TEXT, writers TEXT 
                  
        )
        
        """)     
        self.conn.commit()
    
    def insert_movie(self,movie):
        self.conn.execute("""
        INSERT INTO movies (rank, name, year, rating, genre, certificate, run_time, tagline, budget, box_office, casts, directors, writers)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)                                    
        """,      
        (movie['rank'], movie['name'], movie['year'], movie['rating'], movie['genre'], movie['certificate'], movie['run_time'], movie['tagline'], movie['budget'], movie['box_office'], movie['casts'], movie['directors'], movie['writers'])
        )
    
        self.conn.commit()
        
        
    def add_movies(self):
        with open(self.movie_csv, 'r', encoding = 'utf-8') as f:
        
    
        
    

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
    
    def convert_runtime(self):
        """
        Convert the runtime to minutes
        """
        hours, minutes = 0, 0
        if 'h' in self.run_time:
            hours = int(self.run_time.split('h')[0])  # get the hours
            if 'm' in self.run_time:
                minutes = int(self.run_time.split('h')[1].strip('m'))  # get the minutes
        elif 'm' in self.run_time:
            minutes = int(self.run_time.split('m')[0].strip())
        return hours * 60 + minutes
        
    def matches_filters(self, genre=None, decade=None, min_rating=None, certificate=None, max_runtime=None):
        """ filters the movie"""
        if genre and genre.lower() not in self.genre.lower():
            return False
        if decade:
            decade_start = decade - (decade % 10)  # e.g. 2000, 2010, 2020...
            decade_end = decade_start + 10
            if not (decade_start <= self.year < decade_end):  # Check if year is within the decade range
                return False
        if min_rating and self.rating < min_rating:
            return False
        if certificate and self.certificate.lower() != certificate.lower():
            return False

        total_runtime = self.convert_runtime()
        if max_runtime is not None:  
            if total_runtime > max_runtime:
                return False
        return True
        

    def format_runtime(self):
        """
        returns the run time in its original format (ex:'2h 20m')
        """
        return self.run_time

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
            if movie.matches_filters(genre=genre, min_rating=min_rating, certificate=certificate, max_runtime=max_runtime):
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
            return sorted(recommendations, key=lambda x: x.convert_runtime())
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


if __name__ == "__main__":
    # Load the dataset
    file_path = 'IMDB Top 250 Movies.csv'
    movies_df = pd.read_csv(file_path)

   
    # Create Movie instances from the DataFrame
    movie_list = [
        Movie(
            rank=row['rank'],
            name=row['name'],
            year=row['year'],
            rating=row['rating'],
            genre=row['genre'],
            certificate=row['certificate'],
            run_time=row['run_time'],  # original runtime string - not in minutes for conversion yet
            tagline=row['tagline']
        )
        for _, row in movies_df.iterrows()
    ]
    
