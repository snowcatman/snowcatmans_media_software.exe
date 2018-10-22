import os
import stat                                                                                                             # import statistics module
import time                                                                                                             # import time module
import sys                                                                                                              # import sys module
import re                                                                                                               # import re (matching) module


# beginning of code dont touch.
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
            if (f_e == '.mp4') or (f_e == '.avi') or (f_e == '.flv') or (f_e == '.mkv') or (f_e == '.mov'):
                listoffiles.append(os.path.join(dirpath, file))
# end of code dont touch

# code that matters
    desired_size = 1024 * 1024 * 300  # 300 GBytes

    with open('listoffiles', 'wb') as outfile:
        for x in xrange(desired_size):
            outfile.write(chr(randint(1,255)))
    print ('done')


    # desired_number_of_files = 25
    # for file_number in range(desired_number_of_files):
    #    filename = 'output_file{0:04d}.dat'.format(file_number)
    #    print('filename: {0}'.format(filename))
    #    with open(filename, 'wb') as fout: fout.write(os.urandom(desired_size))
    #print('Done.')


if __name__ == '__main__':
    main()
# end