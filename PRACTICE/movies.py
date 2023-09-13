from movie_module import Movies

movie_title = input("Enter movie name: ")
director_name = input("Enter Director name: ")
movie_genre = input("Enter movie genre: ")
movie_release_year = input("Enter Year of release: ")
movie_duration = int(input("Enter movie duration: "))
movie_rating = input("Enter movie rating: ")
movie_trailer_link = input("Enter movie trailer link: ")

movie1 = Movies(movie_title, director_name, movie_genre, movie_release_year, movie_duration, movie_trailer_link)
movie1.movie_info()
movie1.movie_rating(movie_rating)
movie1.watch_trailer()

