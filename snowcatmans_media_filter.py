import os, string, stat, time, sys, re

#  def has_hidden_attripute(filepath):
#      return bool(os.stat(filepath).st_file_attribute & stat.file_attribute_hidden)

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

# def my_path(path):
  #  for (dirpath, dirnames, filenames) in os.walk(path):
   #     path = (os.path.join(dirpath, dirnames, filenames)
    # pass
    


def FFMF(path): 
    # print('before path', path)
    for (dirpath, dirnames, filenames) in os.walk(path):
        # print('raw dirpath split', dirpath)
        # print('raw dirdirnames split', dirnames)
        # print('raw filenames split', filenames)

        for file in filenames:
            file_name, f_e = os.path.splitext(file)
            f_e = f_e.lower()
            if (f_e == '.mp4') or (f_e == '.avi') or (f_e == '.flv') or (f_e == '.mkv') or (f_e == '.mov'):
                # print('file name')
                # print('its extension', f_e)
                if "trailer" in file_name.lower():
                    this_variable = 101010101010
                else:
                    pathA = dirpath.split(os.sep)
                    parent1 = pathA[-1]
                    parent2 = pathA[-2]
                    # print('step before if season')
                    if "season" in parent1.lower():
                        this_variable = 101010101011
                    else: # movie filter list generater
                        NONO = '\(|\)|\[|\]|\/|\;|\-| 1080dpi'
                        fn = re.sub(NONO, '', file_name)
                        fnparent1 = re.sub(NONO, '', parent1)
                        fnmatchObj1 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4}) ([ a-z0-9A-Z ]+)', fn, re.I)
                        fnmatchObj2 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4}) ([ a-z0-9A-Z ]+)', fnparent1, re.I)
                        matchObj1 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4}) ([ a-z0-9A-Z ]+)', file_name, re.I)
                        matchObj2 = re.match(r'^([ a-z0-9A-Z ]+) (\d{4}) ([ a-z0-9A-Z ]+)', parent1, re.I)
                        if fnmatchObj1 and fnmatchObj2 and fnmatchObj1.group(1) == fnmatchObj2.group(1):
                            FnT = fnmatchObj1.group(1) # file
                            FnTp = fnmatchObj2.group(1) # parent
                            FnY = fnmatchObj1.group(2) # file
                            FnYp = fnmatchObj2.group(2) # parent
                            FnCR = fnmatchObj1.group(3) # file
                            FnCRp = fnmatchObj2.group(3)   # parent  
                            if matchObj1 and matchObj2 and matchObj1.group(1) == matchObj2.group(1):
                                rawT = matchObj1.group(1) # file
                                rawTp = matchObj2.group(1) #parent
                                rawY = matchObj1.group(2) # file
                                rawYp = matchObj2.group(1) # parent
                                rawCR = matchObj1.group(3) # file
                                rawCRp = matchObj2.group(1) # parent
                                # print('before dirpath', dirpath)
                                file = rawT+' '+FnY+' '+FnCR
                                dirpath = rawTp+' '+FnYp+' '+FnCRp
                                # print('after dirpath', dirpath)
                                
                                #  path, dirpath, dirnames, file
                                
                                #  path = (os.path.join(dirpath, file)
                                #  print(path)
                                #  return path
                                #  newpath = []
                                #  path, dirpath, dirnames, file = newpath
                                #  print(newpath)
        #print('after dirnames', dirnames)
        #print('after dirpath', dirpath)
        #print('after file', file)
        # join path
        # return path
        # print('after path', path)

















# commented the rest out in a paragraph comment
'''
                                # at this point we want to rebuild join the file 
                                # structure to make an index for the futere tree view.
                                # print('path = -->', os.path)
                                # print('directoryname >', dirpath)
                                # print('filename', file)

                            if fnparent1 not in listOfMovies:
                                # listOfMovies.append(fnparent1)
                                listOfMovies.append(os.path.join(dirpath, file))
                                # print(str(len(listOfMovies)))
                                # print(listOfMovies)
                            else:
                                listoffiles =[]
                                listoffiles.append(os.path.join(dirpath, file))
                                # path = listoffiles
                                # print(path)
                                # return path

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
'''
# end of file
