# If you want. It would be nice to help me in my leanings to leave obvious notes as to what does what. Then email me the changes you made. thank you.
import os                                                                                                               # import operating system module
import stat                                                                                                             # import statistics module
import time                                                                                                             # import time module
import sys                                                                                                              # import sys module
import re                                                                                                               # import re (matching) module

# function begins
def getlistoffiles(dirname):                                                                                            # create list of files and sub directories

    listoffile = os.listdir(dirname)                                                                                    # names in the given directory
    allfiles = list()

    for entry in listoffile:                                                                                            # iterate over all the entries
        fullpath = os.path.join(dirname, entry)                                                                         # get full path from root to file
        if os.path.isdir(fullpath):                                                                                     # If entry is a directory then get the list
                                                                                                                        # from file in this directory
            allfiles = allfiles + getlistoffiles(fullpath)                                                              # list this file from root to directory
        else:
            allfiles.append(fullpath)                                                                                   # append to this list
    return allfiles                                                                                                     # return to list
# function ends

# begin
def main():
    dirname = os.getcwd()
    # listoffiles = getlistoffiles(dirname)                                                                             # Get the list of all files in directory
                                                                                                                        # tree at given path
    listoffiles = list()
    listOfTvShows = list()
    listOfMovies = list()

    for (dirpath, dirnames, filenames) in os.walk(dirname):                                                             # Get the list of all files in
                                                                                                                        # directory tree at given path
        for file in filenames:
            file_name, f_e = os.path.splitext(file)                                                                     # splitting file name and extension
            f_e = f_e.lower()                                                                                           # making all file extensions lower case
            if (f_e == '.mp4') or (f_e == '.avi') or (f_e == '.flv') or (f_e == '.mkv') or (f_e == '.mov'):             # include these extensions
                if "trailer" in file_name.lower():                                                                      # if trailer is in filename
                    this_variable = 1                                                                                   # make it a variable
                else:
                    path = dirpath.split(os.sep)                                                                        # splitting directory paths from files
                    parent1 = path[-1]                                                                                  # parent to file
                    parent2 = path[-2]                                                                                  # grand parent to file
                    if "season" in parent1.lower():                                                                     # if season is in folder name - lower case

                        # list only perent2 once
                        if parent2 not in listOfTvShows:                                                                # if not in list, continue.
                            listOfTvShows.append(parent2)                                                               # append to list
                        # listOfTvShows.append(os.path.join(dirpath, file))
                    else:
                        #for now list movies that are not tv shows

                        # matchObj1 = re.match(r'^([a-z0-9A-Z\s]+) (\d{4})(.*)', file_name, re.I)                         # find regular expression in file_name
                        # matchObj2 = re.match(r'^([a-z0-9A-Z\s]+) (\d{4})(.*)', parent1, re.I)                           # find regular expression in parent1
                        #if matchObj1 and matchObj2 and matchObj1.group(1) == matchObj2.group(1):                        # if 1 and 2 and 1.group = 2.group continue
                                # listOfMovies.append(os.path.join(dirpath, file))
                                # print(listOfMovies)
                                # wait = input("PRESS ENTER TO CONTINUE.")
                        if parent1 not in listOfMovies:                                                             # if not in list, continue.
                                listOfMovies.append(parent1)                                                        # append to list
                                print(parent1)
                                # listOfMovies.append(os.path.join(dirpath, file))
                        else:
                            listoffiles.append(os.path.join(dirpath, file))

    f = open('mediatext_test.txt', 'w')                                                                                      # create/over_write open file medialist.txt

    tv_output = "\n TV Shows, count: " + str(len(listOfTvShows))                                                        # print tv shows count how many tv shows
    f.write(tv_output)                                                                                                  # write the output to file
    for elem in listOfTvShows:                                                                                          # grab element of list tv shows
        f.write('\n' + elem)                                                                                            # write them to file

    movies_output = "\n Movies, count: " + str(len(listOfMovies))                                                       # print movie shows count how many movie shows
    f.write(movies_output)                                                                                              # write the output to file
    for elem in listOfMovies:                                                                                           # grab element of list movie shows
        f.write('\n' + elem)                                                                                            # write them to file

    f.close()                                                                                                           # close file


if __name__ == '__main__':
    main()
# end

# from snowcatman@gmail.com