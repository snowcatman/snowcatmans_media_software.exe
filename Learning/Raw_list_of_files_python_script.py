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
    listOfFiles = getlistoffiles(dirname)

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    f = open('Raw_list_of_files_python_script.txt', 'w')                                                                                 # create/over_write open file medialist.txt

    files_output = "\n List of all files, count: " + str(len(listOfFiles))
    f.write(files_output)                                                                                               # write the output to file
    for elem in listOfFiles:                                                                                            # grab element of list tv shows
        f.write('\n' + elem)                                                                                            # write them to file
    f.close()                                                                                                           # close file


if __name__ == '__main__':
    main()
# end

# from snowcatman@gmail.com