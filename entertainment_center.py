import media
import fresh_tomatoes

# List of all the movies to feature on the site
jurassic_park = media.Movie("Jurassic park",
                            "An Adventure 65 Million Years in Tte Making",
                            "https://upload.wikimedia.org/wikipedia/"
                            "en/e/e7/Jurassic_Park_poster.jpg",
                            "https://www.youtube.com/watch?v=_IesovZQR4g")

interstellar = media.Movie("Interstellar",
                           "The End of the Earth Will Not be the End of Time",
                           "https://upload.wikimedia.org/wikipedia/"
                           "en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

lego_movie = media.Movie("The Lego Movie",
                         "A Story of a Nobody Who Saved Everybody",
                         "https://upload.wikimedia.org/wikipedia/"
                         "en/1/10/The_Lego_Movie_poster.jpg",
                         "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

bourne_identity = media.Movie("The Bourne Identity",
                              "He Was The Perfect Weapon Until "
                              "He Became The Target",
                              "https://upload.wikimedia.org/wikipedia/"
                              "en/a/ae/BourneIdentityfilm.jpg",
                              "https://www.youtube.com/watch?v=jp4nzjap6I8")

grudge_match = media.Movie("Grudge Match",
                           "When time hits hard, hit harder.",
                           "http://upload.wikimedia.org/wikipedia/"
                           "en/4/4a/Grudge_Match_Poster.jpg",
                           "https://www.youtube.com/watch?v=1bQSOBJCPQE")


# Store movies in a list
movies = [jurassic_park,
          interstellar,
          lego_movie,
          bourne_identity,
          grudge_match]

# Prepare the movie trailer page and load it
fresh_tomatoes.open_movies_page(movies)
