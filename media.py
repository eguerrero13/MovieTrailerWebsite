import webbrowser


class Movie:
    """
    Class representing a movie and its attributes.
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Movie title
        self.title = movie_title

        # Movie story line
        self.storyline = movie_storyline

        # Full url to online poster image
        self.poster_image_url = poster_image

        # Full url to youtube movie trailer
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open new browser and play the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
