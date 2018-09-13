import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A movie that shows the life of a boy´s toys",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

toy_story.show_trailer()

movies = [toy_story]

print(media.Movie.VALID_RATINGS)
fresh_tomatoes.open_movies_page(movies)


