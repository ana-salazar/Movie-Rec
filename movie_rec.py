import sqlite3
import csv
from collections import Counter
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
        CREATE TABLE IF NOT EXISTS movies (
        rank INTEGER PRIMARY KEY, name TEXT, year INTEGER, 
        rating REAL, genre TEXT, certificate TEXT, run_time TEXT, tagline TEXT,
        budget INTEGER, box_office INTEGER, casts TEXT, directors TEXT, writers TEXT 
                  
        )
        
        """)     
        self.conn.commit()
    
    def insert_movie(self,movie):
        self.cursor.execute("""
        INSERT INTO movies (rank, name, year, rating, genre, certificate, run_time, tagline, budget, box_office, casts, directors, writers)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)                                    
        """, movie)
        self.conn.commit()
        
        
    def add_movies(self):
        with open(self.movie_csv, 'r', encoding = 'utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader: 
                movie = (
                int(row['rank']),
                row['name'],    
                int(row["year"]),    
                float(row["rating"]),
                row["genre"],
                row["certificate"],
                row["run_time"],
                row["tagline"],
                int(row["budget"]),
                int(row["box_office"]),
                row["casts"],
                row["directors"],
                row["writers"]    
                    
                )
                self.insert_movie(movie)
    
        self.conn.commit()

class Movie:
    """
    Class representing a movie by its attributes
    """
    def __init__(self, rank, name, year, rating, genre, certificate, run_time, tagline, budget, box_office, casts, directors, writers):
        self.rank = rank
        self.name = name
        self.year = year
        self.rating = rating
        self.genre = genre
        self.certificate = certificate
        self.run_time = run_time #time looks like 2h 20m
        self.tagline = tagline
        self.budget = budget
        self.box_office = box_office
        self.casts = casts
        self.directors = directors
        self.writers = writers
    
    def convert_runtime(self):
        """
        Convert the runtime to minutes
        """
        hours, minutes = 0, 0
        if 'h' in self.run_time:
            hours = int(self.run_time.split('h')[0])  # get the hours
            if 'm' in self.run_time:
                minutes = int(self.run_time.split('h')[1].strip('m'))  # get the minutes
            else:
                minutes = 0
        elif 'm' in self.run_time:
            minutes = int(self.run_time.split('m')[0].strip())
        return hours * 60 + minutes
        
    def format_runtime(self):
        """
        returns the run time in its original format (ex:'2h 20m')
        """
        total_mins = self.convert_runtime()
        hours = total_mins // 60
        minutes = total_mins % 60
    
        if hours > 0 and minutes > 0:
            return f'{hours}h {minutes}m'
        if hours > 0 and minutes == 0:
            return f"{hours}"    
        
    def matches_filters(self, rank=None, genre=None, decade=None, min_rating=None, year=None,certificate=None, max_runtime=None, casts=None, directors=None):
        """ filters the movie"""
        
        if rank and self.rank != rank:
            return False
        
        if genre and genre.lower() not in self.genre.lower():
            return False
        
        if decade:
            decade_start = decade - (decade % 10)  # e.g. 2000, 2010, 2020...
            decade_end = decade_start + 10
            if not (decade_start <= self.year < decade_end):  # Check if year is within the decade range
                return False
        if year:
            if self.year != year:
                return False
        
        if certificate and self.certificate.lower() != certificate.lower():
            return False
        
        if min_rating and self.rating < min_rating:
            return False

        total_runtime = self.convert_runtime()
        if max_runtime is not None:  
            if total_runtime > max_runtime:
                return False
            
        if casts and casts.lower() not in self.casts.lower():
            return False
        
        if directors and directors.lower() not in self.directors.lower():
            return False
        
        return True
        

class MovieRecommender:
    """
    Class to handle movie recommendation logic
    """
    def __init__(self, movie_list):
        self.movies = movie_list

    def recommend_movies(self, rank=None, genre=None, decade=None, min_rating=None, certificate=None, max_runtime=None, casts=None, directors=None, sort_by=None):
        """
        Recommend movies based on filters and optionally sort the results.
        """
        recommendations = []
        for movie in self.movies:
            if movie.matches_filters(genre=genre, min_rating=min_rating, certificate=certificate, max_runtime=max_runtime, casts=casts, directors=directors):
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
    movie_db = MovieDatabase() #initialize movie database

   
    # Create Movie instances from the DataFrame
    movie_list = []
    cursor = movie_db.conn.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    for row in rows:
        movie_list.append(Movie(*row)) #using * to get everything in the row
    
    #create instance of MovieRecommender
    recommender = MovieRecommender(movie_list)
    recommendations = recommender.recommend_movies(min_rating= 9, genre = "Action")