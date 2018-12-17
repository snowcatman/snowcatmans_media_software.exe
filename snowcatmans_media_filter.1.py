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

def AMy_Folder_File_Filter(folderfilelist):
    # dirnames = folderfilelist
    # print(dirnames)
    return folderfilelist

def My_Folder_File_Filter(path): 
    dirpath = list()
    dirnames = list()
    filenames = list()
    listOfTvShows = list()
    listOfMovies = list()
    
    # print('step 1')
    print(path)
    for (dirpath, dirnames, filenames) in os.walk(path):
        # print('step 2')
        for file in filenames:
            file_name, f_e = os.path.splitext(file)
            f_e = f_e.lower()
            if (f_e == '.mp4') or (f_e == '.avi') or (f_e == '.flv') or (f_e == '.mkv') or (f_e == '.mov'):
                
                if "trailer" in file_name.lower():
                    this_variable = 1
                else:
                    
                    pathA = dirpath.split(os.sep)
                    parent1 = pathA[-1]
                    parent2 = pathA[-2]
                    # print('step before if season')
                    if "season" in parent1.lower():

                        #list only perent2 once
                        if parent2 not in listOfTvShows:
                            listOfTvShows.append(parent2)
                        listOfTvShows.append(os.path.join(dirpath, file))

                    else:
                        print('before matchObj1 --->', file_name)
                        matchObj1 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4}) ([ a-z0-9A-Z ]+)', file_name, re.I)
                        print('print after matchObj1 --->', matchObj1)
                        # print(matchObj1.expand())
                        matchObj2 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4}) ([ a-z0-9A-Z ]+)', parent1, re.I)
                        print('step 1')
                        if matchObj1 and matchObj2 and matchObj1.group(1) == matchObj2.group(1):
                            print('step 2', matchObj1)
                            print('step 3 group 3', matchObj1.group(3))
                            print('um, start ------>', matchObj1.start())
                            listOfMovies.append(os.path.join(dirpath, file))
                            #p rint(listOfMovies)
                            # wait = input("PRESS ENTER TO CONTINUE.")
                            if parent1 not in listOfMovies:
                                listOfMovies.append(parent1)
                                # print(listOfMovies)
                                listOfMovies.append(os.path.join(dirpath, file))
                            else:
                                listoffiles =[]
                                listoffiles.append(os.path.join(dirpath, file))
                                path = listoffiles
                                return path



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
            if (f_e == '.mp4') or (f_e == '.avi') or (f_e == '.flv') or (f_e == '.mkv') \
                or (f_e == '.mov'):
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


                        matchObj1 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4})(f_e)', \
                            file_name, re.I)          #
                        matchObj2 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4})(f_e)', \
                            parent1, re.I)
                        if matchObj1 and matchObj2 and matchObj1.group(1) == \
                            matchObj2.group(1):
                            listOfMovies.append(os.path.join(dirpath, file))
                            # print(listOfMovies)
                            # wait = input("PRESS ENTER TO CONTINUE.")
                            if parent1 not in listOfMovies:
                                listOfMovies.append(parent1)
                                # listOfMovies.append(os.path.join(dirpath, file))
                            else:
                                listoffiles.append(os.path.join(dirpath, file))
