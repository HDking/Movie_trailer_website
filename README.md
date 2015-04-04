#Welcome to the README file of the movie trailer website made for the Udacity course

In this folder you can find different files that together make the movie trailer
website. The main four documents are: 

## 1. fresh_tomatoes.html

This file contains the output html file which can be run on your browser. 
Download the file and run it by double clicking it. 

## 2. fresh_tomatoes.py

This file creates the above mentioned html file. It has two functions:
a. `create_movie_tiles_content(movies)` : takes an array attribute which creates the tiles 
shown in the html file, for the movies stored in `movies`
b. `open_movies_page(movies)`:takes an array `movies` and creates the above html file and
opens it in a new browser tab. 

## 3. `media.py`

Here the class Movie is defined storing different information about the movie. 

##4. `entertainment_center.py`: 

This is the file storing all the instances of the class Movie. 
Next to that the array `movies` is stored here. This is the file to run when creating a 
new version of `fresh_tomatoes.html`. 
