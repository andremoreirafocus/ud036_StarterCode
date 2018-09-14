import media
import fresh_tomatoes

# Instantiate the class Movie to create an object for each movie
toy_story = media.Movie("Toy Story",
                        "A movie that shows the life of a boy´s toys",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

mission_impossible = media.Movie("Mission Impossible - Fallout",
                                 "The best action movie of all times",
                                 "http://br.web.img3.acsta.net/r_1920_1080/pictures/18/05/14/17/09/5117345.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=wb49-oV0F78")

vingadores_guerra_infinita = media.Movie("Vingadores - Guerra Infinita",
                                 "Os Vingadores enfrentam Thanus",
                                 ("https://cdn.ome.lt/CI0iJ7ZvvIhGcIkC46loYJx"
                                 "ZSnA=/200x0/smart/extras/capas/PosterGuerraInfinita.jpg"),  # NOQA
                                 "https://www.youtube.com/watch?v=t_ULBP6V9bg")
mega_tubarao = media.Movie("Mega Tubarao",
                           "A tripulação de um submarino é atacada por uma"
                           "criatura pré-histórica, um tubarão de 20 metros",
                           "https://cinepop.com.br/wp-content/uploads/2018/07/megatubar%C3%A3o1.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=hgwycIPilI0")


hotel_artemis = media.Movie("Hotel Artemis",
                            "O Hotel Artemis é uma espécie de hospital de"
                            "assassinos",
                            "https://vertentesdocinema.com/wp-content/uploads/2018/09/hotel-artemis-cartaz-206x300.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=JqfuKsoEEms")

deus_nao_morto = media.Movie("Deus nao esta morto",
                             "Uma batalha entre a fé e a razão",
                             "http://www.claquete.com/fotos/filmes/poster/11012_medio.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=wIKExeMVksk")

# Creates a list of Movie objects so that fresh_tomatoes.open_movies_page can
# generate the web site
movies = [toy_story, mission_impossible, vingadores_guerra_infinita,
          mega_tubarao, hotel_artemis, deus_nao_morto]

# Renders and opens the web page that contains the movie posters and the links
# to the youtube movie trailers
fresh_tomatoes.open_movies_page(movies)
