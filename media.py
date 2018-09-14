import webbrowser


class Movie():
"""This class creates a movie object that has the following properties:
        title(string): the movie´s title name
        storyline(string): a brief description of the movie story
        poster_image_url(string): the URL of the poster image file
        trailer_youtube_url(string): the URL of the movie´s youtube trailer         
       
"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """This method initializes object properties for the class

        Args:
            movie_title (string): the movie´s title name
            movie_storyline (string): a brief description of the movie story
            poster_image (string): the URL of the poster image file
            trailer_youtube (string): the URL of the movie´s youtube trailer 

        Returns:
            Does not return any value
            
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This method opens the web browser and plays the youtube trailer for
            the movie

        Args:
            Does not have any arguments
        
        Returns:
            Does not return any value

        """
        webbrowser.open(self.trailer_youtube_url)
        

        
