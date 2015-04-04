import media
import fresh_tomatoes

#instances of the Movie class
saving_private_ryan = media.Movie("Saving Private Ryan", "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.", "http://ia.media-imdb.com/images/M/MV5BNjczODkxNTAxN15BMl5BanBnXkFtZTcwMTcwNjUxMw@@._V1_SY317_CR9,0,214,317_AL_.jpg",
"https://www.youtube.com/watch?v=zwhP5b4tD6g", "Tom Hanks")

up = media.Movie("UP", "To avoid being taken away to a nursing home, an old widower tries to fly his home to Paradise Falls, South America, along with a boy scout who accidentally lifted off with him.", "http://www.movieposterdb.com/posters/09_04/2009/1049413/l_1049413_0faf87e5.jpg", "https://www.youtube.com/watch?v=qas5lWp7_R0", "Edward Asner")

coach_carter = media.Movie("Coach Carter", "Coach drives discipline to difficult high school kids and turns it into a winning team", "http://ia.media-imdb.com/images/M/MV5BMTIwMTc1MDQ1Nl5BMl5BanBnXkFtZTcwNDk3NzcyMQ@@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=znyAnWUYf2g", "Samuel L. Jackson")

school_of_rock = media.Movie("School of Rock", "When struggling musician Dewey Finn finds himself out of work, he takes over his roommate's job as an elementary school substitute teacher and turns class into a rock band.", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=3PsUJFEBC74", "Jack Black")

ratatouille = media.Movie("Ratatouille", "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.","http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk","Brad Garrett")

hunger_games = media.Movie("Hunger Games", "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.", "http://www.movieposterdb.com/posters/12_02/2012/1392170/l_1392170_7bed9f27.jpg", "https://www.youtube.com/watch?v=PbA63a7H0bo", "Jennifer Lawrence")

#contains the list rendered to the screen
movies = [saving_private_ryan, up, school_of_rock, coach_carter, ratatouille, hunger_games, up, coach_carter, ratatouille]
#calls the function open_movies_pages with the movies array to render the page
fresh_tomatoes.open_movies_page(movies)
