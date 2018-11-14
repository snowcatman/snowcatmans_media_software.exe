# Shawn Quintal email @ snowcatman@gmail.com
# beginning of file example2.py
import os                   # imports the os module
from imdb import IMDb       # imports IMDB function from module imdb

# I am woundering if I can have a chat with anyone about imdbpy? I have created a database from imdb.com dataset
# files and I am accessing it. I am attempting to learn about the way I access it. So I can get information and
# proccess it. It, seem the mixed syntax of sql imdbpy and python, is troupling me. In a way that I am not 
# understanding. An example is how to get the year out of a movie. Here is what i have so far. with a 
# instructional link first then what I have so far. 
# Link to instruction web site.
# https://imdbpy.readthedocs.io/en/latest/usage/s3.html

# begin user input prompt
os.system('cls'), # clears windows cmd.exe screen
MyMovieSearch = input('\n What is the movie title you want to search for? : ')
# the ubove line: create a string from users input in a tuple object
# print(MyMovieSearch) # print string from tuple

# I would like to get the unknown movie - title, startYear, runtimeMinutes and movie rating. For now.
# If it does not have the info, return null or none and/or leave a "'_'" for the missing info.
# I have been making attempts to understand how to get and use keys to get the information.

print(); print(" ---------------------Your Movie----->(", MyMovieSearch, ")<--Seeking")
print()
# the above two lines just help confirm to the  user there print out of there movie. by printing the tuple object
# end user input prompt

# begin movie search
ia = IMDb('s3', 'sqlite:///c:\\python3_imdb_learning_area\\imdb\\imdb.db', adultSearch=0)
# the above line: uses the IMDB module, to make a tuple of strings using the s3 module as argument one,
# and use sqlite module to access database for read/write as argument two.

results = ia.get_movie(MyMovieSearch)
# The above line: creates a string or a list of strings from the ia object as another tuple object.
# The above line to be explained further. i.e "ia.search_movie".
# Now I have seen something like this before, and want to know more about how to use it to get my info.
# And what other options I my have.
# for result in results:
    # for each string in tuple list
print(results) # I am woundering what function is going to give me a startYear
    # print each strings result/movieID and result (of the user search movie)

# playing with exaple from linked web site.
# for movie in results:
#    print(movie.movieID, movie['smart long imdb canonical title'])
#    print('==== "%s" / movie_id: %s ====' % (movie['startYear'], movie_id))
#    print(movie.movieID)
#    movie_id = ia.get_movie(movie.movieID)
#    print(movie_id)

#    print(movie.movieID, movie, movie['title_basic_startYear'])
# Retrieves default information for the first result (a Movie object).
# the_unt = results[0]
# ia.update(the_unt)

# Print some information.
# print(the_unt)
# print(the_unt['runtime'])
# print(the_unt['rating'])
# print(the_unit['startYear'])

# MyMovieSearch = results[0]
# ia.update(MyMovieSearch)
# print(MyMovieSearch.keys())

#end movie search

# start of copy/paste
#
#    What is the movie title you want to search for? : wonderwoman
#
#    ---------------------Your Movie----->( wonderwoman )<--Seeking
#
#   8408184 Wonder Woman 2014
#   Traceback (most recent call last):
#     File "example2.py", line 47, in <module>
#       print(movie.movieID, movie, movie['startYear'])
#     File "C:\Program Files (x86)\Python37-32\lib\site-packages\imdb\utils.py", line 1495, in __getitem__
#       rawData = self.data[key]
#   KeyError: 'startYear'
#
#   c:\python3_imdb_learning_area>
#end of copy/paste


# end of file example2.py
exit()