# Project: Movie Trailer Website

The Movie Trailer Website project consists of server-side code to store a list of movies titles, along with its respective box art imagery and movie trailer website. The data should be served as a web page allowing visitors to review the movies and watch the trailers

## Usage

Import media and fresh_tomatoes libraries:
```sh
import media
import fresh_tomatoes
```

Create movie objects:
```sh
movie1 = media.Movie("Movie title",
                 "Movie description",
                 "http://poster_url",
                 "http://youtube_trailer_url")
movie2 = media.Movie(...
```

Create array with movies:
```sh
movies = [movie1, movie2, ...]
```

Create webpage:
```sh
fresh_tomatoes.open_movies_page(movies)
```

## Creator
* Einar Guerrero