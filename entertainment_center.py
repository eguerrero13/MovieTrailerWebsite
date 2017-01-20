import media
import fresh_tomatoes

# Create PI movie object
pi = media.Movie("PI: faith in chaos",
                 "The story about a mathematician and the obsession with "
                 "mathematical regularity contrasts two seemingly "
                 "irreconcilable entities: the imperfect, irrational "
                 "humanity and the rigor and regularity of mathematics, "
                 "specifically number theory.",
                 "https://upload.wikimedia.org/wikipedia/en/5/5a/Piposter.jpg",
                 "https://www.youtube.com/watch?v=GsAHXMcXgFA")

# Create School of Rock movie object
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# Create Dobermann movie object
dobermann = media.Movie("Dobermann",
                        "The charismatic criminal Dobermann, leads a gang of "
                        "brutal robbers.",
                        "https://upload.wikimedia.org/wikipedia/en/1/17/DobermannPoster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=eijRyGWoSW4")

# Create The Godfather movie object
godfather = media.Movie("The Godfather",
                        "Chronicles the family under the patriarch Vito "
                        "Corleone",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=sY1S34973zA")

# Create Pulp Fiction movie object
pulp_fiction = media.Movie("Pulp Fiction",
                           "Connects intersecting storylines of LA mobsters, "
                           "fringe players and small-time criminals",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Create Requiem For A Dream movie object
requiem_dream = media.Movie("Requiem for a Dream",
                            "The film depicts four different forms of drug "
                            "addiction",
                            "https://upload.wikimedia.org/wikipedia/en/9/92/Requiem_for_a_dream.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=jzk-lmU4KZ4")

# Create array and add movies to it
movies = [dobermann, godfather,
          pi, school_of_rock,
          pulp_fiction, requiem_dream]

# Create webpage with favorite movies array
fresh_tomatoes.open_movies_page(movies)
