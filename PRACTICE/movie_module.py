# create a class for movies
class Movies:
    def __init__(self, title, director, genre, year_of_release, duration, trailer):
        self.title = title
        self.director = director
        self.genre = genre
        self.year_of_release = year_of_release
        self.duration = duration
        self.trailer = trailer
        self.ratings = []

    def movie_info(self):
        print("Title: {}".format(self.title))
        print("Director: {}".format(self.director))
        print("Genre: {}".format(self.genre))
        print("Year of release: {}".format(self.year_of_release))
        print("Duration: {} minutes".format(self.duration))

    def watch_trailer(self):
        print("Watch {} trailer on Youtube at {}".format(self.title, self.trailer))

    def movie_rating(self, rating):
        if 0 < rating <= 10:
            self.ratings.append(rating)
            s = [str(i) for i in self.ratings]
            print("Rating:", s)
        else:
            print("Ratings should be between 0 and 10")


