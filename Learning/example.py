# Shawn Quintal email @ snowcatman@gmail.com
# beginning of file example.py getting ready for post processing media files.
import os                   # imports the os module
import sys                  # import the sys module
import time                 # import the time module
from imdb import IMDb       # imports IMDB function from module imdb Note could not find the module in python software
                            # folder. I need to clerify my understanding of modules and functions

# I am woundering if I can have a chat with anyone about imdbpy? I have created a database from imdb.com dataset
# files and I am accessing it. I am attempting to learn about the way I access it. So I can get information and
# proccess it. It, seem the mixed syntax of sql imdbpy and python, is troupling me. In a way that I am not
# understanding. An example is how to get the year out of a movie. Here is what i have so far. with a
# instructional link first then what I have so far.
# Link to instruction web site.
# https://imdbpy.readthedocs.io/en/latest/usage/s3.html
# https://imdbpy.readthedocs.io/en/latest/index.html
# https://imdbpy.readthedocs.io/en/latest/usage/ptdf.html
# https://imdbpy.readthedocs.io/en/latest/usage/data-interface.html

# begin user input prompt
os.system('cls'), # clears windows cmd.exe screen
print()
print("                    Beginning example.py")
time.sleep(1)
os.system('cls'), # clears windows cmd.exe screen
My_path = "C:\python3_imdb_learning_area\media_temp_list.txt"
if os.path.isfile(My_path):
#    print("True")
    print()
    print("      cleaning file -- media_temp_list.txt")
    f = open('media_temp_list.txt', 'w')
    f.write('')
    f.close()
    print("      ready...")
else:
#    print("False")
    print("    will create or append to --  media_temp_list.txt")
time.sleep(2)
os.system('cls'), # clears windows cmd.exe screen
MyMovieSearch = input('\n What is the movie title you want to search for? : ')
# the above line: create a string from users input in a tuple object
# print(MyMovieSearch) # print string from tuple

# I would like to get the unknown movie - title, startYear, runtimeMinutes and movie rating. For now.
# If it does not have the info, return null or none and/or leave a "'_'" for the missing info.
# I have been making attempts to understand how to get and use keys to get the information.

print(); print(" ---------------------Your Movie----->(", MyMovieSearch, ")<--Seeking")
print("working...")
print()
# the above two lines just help confirm to the  user there print out of there movie. by printing the tuple object
# end user input prompt

# begin movie search
ia = IMDb('s3', 'sqlite:///c:\\python3_imdb_learning_area\\imdb\\imdb.db')
# the above line: uses the IMDB module, to make a tuple of strings using the s3 module as argument one,
# and use sqlite module to access database for read/write as argument two.


results = ia.search_movie(MyMovieSearch)

# The above line: creates a string or a list of strings from the ia object as another tuple object.
# The above line to be explained further. i.e "ia.search_movie".
# Now I have seen something like this before, and want to know more about how to use it to get my info.
# And what other options I my have.
for result in results:
    #for something in something???
    print(result.movieID)
    # expected more of the results: title, year, rating, and any other info associated with the title.
    # I have been doing a mix of other functions to get the startYear but no success.


    results1 = ia.get_movie(result.movieID)
    orig_stdout = sys.stdout
    f = open('media_temp_list.txt', 'a')
    sys.stdout = f
    print("===================================================")
    print(results1)
    print("(", results1.get('year'), ")<-->(", results1.get('startYear'), ")  <------ year vs. startYear")
    print()
    print("genres-------------->", results1.get('genres'))
    
    print("akas---------------->", results1.get('akas'))

    print("kind---------------->", results1.get('kind'))
    print("title--------------->", results1.get('title'))
    print("original title------>", results1.get('original title'))
    print("runtimes------------>", results1.get('runtimes'))
    print("director------------>", results1.get('director'))
    print("writer-------------->", results1.get('writer'))
    print("ordering------------>", results1.get('ordering'))
    print("rating-------------->", results1.get('rating'))
    print()
    print("imdb keys----------->", results1.infoset2keys)
    print()
    print(results1.current_info)
    print()
    print("---------------new line-----------------")
    print()
    sys.stdout = orig_stdout
    f.close()
#    print("Finnished -- file -- media_temp_list.txt -- is ready -- in the loop")
# print("test")
# print("Finnished -- file -- media_temp_list.txt -- is ready -- out of loop")
# end movie search
os.system('cls'), # clears windows cmd.exe screen
print()
print("                    end of module example.py")
time.sleep(1)
os.system('cls')

# begin copy/paste

#    What is the movie title you want to search for? : supergirl
#
#    ---------------------Your Movie----->( supergirl )<--Seeking
#   working...
#
#   8814476
#   7981448
#   6837238
#   6537530
#   5912646
#   4872854
#   4397094
#   4016454
#   Traceback (most recent call last):
#     File "example.py", line 82, in <module>
#       print("akas---------------->", results1.get('akas'))
#     File "C:\Program Files (x86)\Python37-32\lib\encodings\cp1252.py", line 19, in encode
#       return codecs.charmap_encode(input,self.errors,encoding_table)[0]
#   UnicodeEncodeError: 'charmap' codec can't encode characters in position 44-54: character maps to <undefined>
#
#   c:\python3_imdb_learning_area>

# end copy/paste

# ========================================================

# begin copy/paste media_temp_list.txt

#    Supergirl
#    ( None )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['action']
#    akas----------------> None
#    kind----------------> movie
#    title---------------> Supergirl
#    original title------> Supergirl
#    runtimes------------> None
#    director------------> None
#    writer--------------> [<Person id:3349927[s3] name:_Oren Uziel_>]
#    ordering------------> 1
#    rating--------------> None
#
#    imdb keys-----------> {'main': ['genres', 'kind', 'title', 'original title', 'adult', 'writer', 'job', 'ordering', 'category', 'nconst']}
#
#    ['main', 'plot']
#
#    ---------------new line-----------------
#
#
#    SuperGirl
#    ( 2018 )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['drama', 'short']
#    akas----------------> [{'region': 'IT', 'ordering': 1, 'title': 'SuperGirl'}, {'ordering': 2, 'types': ['original'], 'title': 'SuperGirl', 'original': True}, {'ordering': 3, 'types': ['working'], 'title': 'ProjectX'}]
#    kind----------------> short
#    title---------------> SuperGirl
#    original title------> SuperGirl
#    runtimes------------> [3]
#    director------------> [<Person id:157178[s3] name:_Max Chicco_>]
#    writer--------------> [<Person id:157178[s3] name:_Max Chicco_>, <Person id:4171284[s3] name:_Simona Rapello_>]
#    ordering------------> 1
#    rating--------------> None
#
#    imdb keys-----------> {'main': ['genres', 'kind', 'title', 'original title', 'adult', 'runtimes', 'year', 'director', 'writer', 'ordering', 'category', 'characters', 'nconst', 'akas']}
#
#    ['main', 'plot']
#
#    ---------------new line-----------------
#
#
#    Supergirl
#    ( 2016 )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['comedy']
#    akas----------------> [{'region': 'US', 'ordering': 1, 'title': 'Supergirl'}]
#    kind----------------> episode
#    title---------------> Supergirl
#    original title------> Supergirl
#    runtimes------------> None
#    director------------> None
#    writer--------------> None
#    ordering------------> 1
#    rating--------------> 8.4
#
#    imdb keys-----------> {'main': ['genres', 'kind', 'title', 'original title', 'adult', 'year', 'directors', 'ordering', 'category', 'characters', 'nconst', 'rating', 'votes', 'akas']}
#
#    ['main', 'plot']
#
#    ---------------new line-----------------
#
#
#    Supergirl
#    ( 2011 )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['music', 'short']
#    akas----------------> [{'region': 'US', 'ordering': 1, 'title': 'Supergirl'}]
#    kind----------------> video
#    title---------------> Supergirl
#    original title------> Supergirl
#    runtimes------------> [4]
#    director------------> [<Person id:6489846[s3] name:_Kevin Wendell Jones_>]
#    writer--------------> [<Person id:6489846[s3] name:_Kevin Wendell Jones_>]
#    ordering------------> 1
#    rating--------------> None
#
#    imdb keys-----------> {'main': ['genres', 'kind', 'title', 'original title', 'adult', 'runtimes', 'year', 'director', 'writer', 'ordering', 'category', 'characters', 'nconst', 'akas']}
#
#    ['main', 'plot']
#
#    ---------------new line-----------------
#
#
#    Supergirl
#    ( 2016 )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['short']
#    akas----------------> None
#    kind----------------> short
#    title---------------> Supergirl
#    original title------> Supergirl
#    runtimes------------> None
#    director------------> [<Person id:4012098[s3] name:_Olivier Mathieu_>]
#    writer--------------> [<Person id:4012098[s3] name:_Olivier Mathieu_>]
#    ordering------------> 1
#    rating--------------> None
#
#    imdb keys-----------> {'main': ['genres', 'kind', 'title', 'original title', 'adult', 'year', 'director', 'writer', 'ordering', 'category', 'characters', 'nconst']}
#
#    ['main', 'plot']
#
#    ---------------new line-----------------
#
#
#    Supergirl
#    ( 2013 )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['drama', 'mystery', 'short']
#    akas----------------> [{'region': 'US', 'ordering': 1, 'title': 'Supergirl'}]
#    kind----------------> short
#    title---------------> Supergirl
#    original title------> Supergirl
#    runtimes------------> [5]
#    director------------> [<Person id:5225627[s3] name:_Aleksandar Adzic_>]
#    writer--------------> [<Person id:5225627[s3] name:_Aleksandar Adzic_>, <Person id:4594601[s3] name:_Christian Kemabia_>]
#    ordering------------> 1
#    rating--------------> None
#
#    imdb keys-----------> {'main': ['genres', 'kind', 'title', 'original title', 'adult', 'runtimes', 'year', 'director', 'writer', 'ordering', 'category', 'characters', 'nconst', 'akas']}
#
#    ['main', 'plot']
#
#    ---------------new line-----------------
#
#
#    Supergirl
#    ( 2016 )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['documentary']
#    akas----------------> [{'region': 'CA', 'ordering': 1, 'title': 'Supergirl'}]
#    kind----------------> movie
#    title---------------> Supergirl
#    original title------> Supergirl
#    runtimes------------> [80]
#    director------------> [<Person id:3492557[s3] name:_Jessie Auritt_>]
#    writer--------------> None
#    ordering------------> 1
#    rating--------------> 6.8
#
#    imdb keys-----------> {'main': ['genres', 'kind', 'title', 'original title', 'adult', 'runtimes', 'year', 'director', 'ordering', 'category', 'nconst', 'rating', 'votes', 'akas']}
#
#    ['main', 'plot']
#
#    ---------------new line-----------------
#
#
#    Supergirl
#    ( 2015 )<-->( None )  <------ year vs. startYear
#
#    genres--------------> ['action', 'adventure', 'drama']
#    akas---------------->
# end copy/paste media_temp_list.txt

# end of file example.py
exit()