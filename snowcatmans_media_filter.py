import os
import stat
import time
import sys
import re

def has_hidden_attripute(filepath):
    return bool(os.stat(filepath).st_file_attribute & stat.file_attribute_hidden)


def getlistoffiles(dirname):
    listoffile = os.listdir(dirname)
    allfiles = list()
    for entry in listoffile:
        fullpath = os.path.join(dirname, entry)
        if os.path.isdir(fullpath):
            allfiles = allfiles + getlistoffiles(fullpath)
        else:
            allfiles.append(fullpath)
    return allfiles

def seperator(folderfilelist): # 
    dirname = folderfilelist
    listOfTvShows = list()
    listOfMovies = list()

    for (dirpath, dirnames, filenames) in os.walk(dirname):
        for file in filenames:
            file_name, f_e = os.path.splitext(file)
            f_e = f_e.lower()
            if (f_e == '.mp4') or (f_e == '.avi') or (f_e == '.flv') or (f_e == '.mkv') or (f_e == '.mov'):
                if "trailer" in file_name.lower():
                    this_variable = 1
                else:
                    path = dirpath.split(os.sep)
                    parent1 = path[-1]
                    parent2 = path[-2]
                    if "season" in parent1.lower():

                        #list only perent2 once
                        if parent2 not in listOfTvShows:
                            listOfTvShows.append(parent2)
                        # listOfTvShows.append(os.path.join(dirpath, file))
                    else:


                        matchObj1 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4})(f_e)', file_name, re.I)          #
                        matchObj2 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4})(f_e)', parent1, re.I)
                        if matchObj1 and matchObj2 and matchObj1.group(1) == matchObj2.group(1):
                            listOfMovies.append(os.path.join(dirpath, file))
                            # print(listOfMovies)
                            # wait = input("PRESS ENTER TO CONTINUE.")
                            if parent1 not in listOfMovies:
                                listOfMovies.append(parent1)
                                # listOfMovies.append(os.path.join(dirpath, file))
                            else:
                                listoffiles.append(os.path.join(dirpath, file))
    pass

def exampleofoldmain():
    dirname = os.getcwd()
    listoffiles = getlistoffiles(dirname)
    listoffiles = list()
    listOfTvShows = list()
    listOfMovies = list()

    for (dirpath, dirnames, filenames) in os.walk(dirname):
        for file in filenames:
            file_name, f_e = os.path.splitext(file)
            f_e = f_e.lower()
            if (f_e == '.mp4') or (f_e == '.avi') or (f_e == '.flv') or (f_e == '.mkv') or (f_e == '.mov'):
                if "trailer" in file_name.lower():
                    this_variable = 1
                else:
                    path = dirpath.split(os.sep)
                    parent1 = path[-1]
                    parent2 = path[-2]
                    if "season" in parent1.lower():

                        #list only perent2 once
                        if parent2 not in listOfTvShows:
                            listOfTvShows.append(parent2)
                        # listOfTvShows.append(os.path.join(dirpath, file))
                    else:


                        matchObj1 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4})(f_e)', file_name, re.I)          #
                        matchObj2 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4})(f_e)', parent1, re.I)
                        if matchObj1 and matchObj2 and matchObj1.group(1) == matchObj2.group(1):
                            listOfMovies.append(os.path.join(dirpath, file))
                            # print(listOfMovies)
                            # wait = input("PRESS ENTER TO CONTINUE.")
                            if parent1 not in listOfMovies:
                                listOfMovies.append(parent1)
                                # listOfMovies.append(os.path.join(dirpath, file))
                            else:
                                listoffiles.append(os.path.join(dirpath, file))

def main()
    #test if fakefolderfile is movie tvmovie or tvshow

    # this is a test folder and file
FakefolderFile = \
    ('C:\\mymovies\\B\\The Best Movie Ever 2018 PG\\The Best Movie Ever 2018 PG.mp4')
    seperator(FakefolderFile)
    print(seperator)
    pass

 if __name__ == "__main__":
    run.main()
