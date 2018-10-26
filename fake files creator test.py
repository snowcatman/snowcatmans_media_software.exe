# beginning of file
# My Beginning Notes:
# Because I am making this module(python script) portable, it should work in what ever directory its in at this time. 10/20/2018
# However, I am thinking of using this code in the future. So imagine if you will that I need to write the functions
# for other modules as well. So don't expect this to stay that way. thank you.
# I use plex server for my media. what I am doing is playing with file and folder names. but plex can
# not see the files if there under 300mb. I used robocopy to create these directories and files from my media
# collection. What I have are a bunch of zero(empty) files in there own directories now. Because I dont want
# to go throe the process again with robocopy(what seem to take overnight). I am using this opportunity to learn a
# little more python. I am also thinking this idea can be used in the future for (snwcatmans_media_software.exe).
# this module is called from windows 10 command prompt or console if you like. and i have python versions 2 and 3 installed
# python 3 is updated and other modules installed(such as: Kivy). At the moment i am using pycharm as my editor.
# Can you tell I am a total beginner.

# I guess I need to import other usfull tools from other modules? i still need to read up on modules.
import os                       # import os module
import os.path                  # import os.path module
import shutil                   # import shutil module
import stat                     # import statistics module
import time                     # import time module
import sys                      # import sys module (Noting: that my editor thinks there is no sys module)
import re                       # import re module
import pandas as pd             # import pandas module as "pd"
import numpy as np              # import numpy module as "np"
import random                   # import random module
from pathlib import Path        # from module pathlib import path function
from tqdm import tqdm, trange   # from module tqdm import tqdm and trange functions
from time import sleep          # from module time import sleep function

# list of media file extensions in (video_exts). Grabed from:
# https://searchcode.com/codesearch/view/95452999/ if you know of any other video file extensions please let me know.
video_exts = ['.3g2', '.3gp', '.asf', '.asx', '.avc', '.avi', '.avs', '.bin', '.bivx', '.divx', '.dv', '.dvr-ms', '.evo',
              '.fli', '.flv', '.img', '.iso', '.m2t', '.m2ts', '.m2v', '.m4v', '.mkv', '.mov', '.mp4', '.mpeg', '.mpg',
              '.mts', '.nrg', '.nsv', '.nuv', '.ogm', '.ogv', '.tp', '.pva', '.qt', '.rm', '.rmvb', '.sdp', '.swf',
              '.svq3', '.strm', '.ts', '.ty', '.vdr', '.viv', '.vp3', '.wmv', '.wpl', '.wtv', '.xsp', '.xvid', '.webm', '.ifo']

# so I need to make a list of all the files that this module(python script) is in from root to file.
# I know this all can really be shortened up, but would I be learning anything. But really. If you would,
# please leave me an example of all this shortened up. maybe in another file with notes explaining
# whats going on and how to compare from each file. thank you.

# ignore these files
system_file_ignore = ['.py', 'empty_templet_file.mp4']
temp_file = 'empty_templet_file.mp4'

# begin function "getlistoffiles" works well do not change.
def getlistoffiles(dirname):                                    # to create list of files and sub directories from root to file.
    listoffile = os.listdir(dirname)                            # create "listoffile" and populate a string of the given directory
    allfiles = []                                               # make a empty list called allfiles
    for entry in listoffile:                                    # iterate over all the "entries" in the "listoffile" list
        fullpath = os.path.join(dirname, entry)                 # get "entry"(in this case the file name(string)) and join it to
                                                                # the "dirname(string)" in the list
        if os.path.isdir(fullpath):                             # If a directory then get full path string to directory
                                                                # from root to directory
            allfiles = allfiles + getlistoffiles(fullpath)      # take "allfiles" list and "getlistoffiles(fullpath)" and
                                                                # add them together
        else:                                                   # if else then
            allfiles.append(fullpath)                           # append list "allfiles" with "fullpath" list.
    return allfiles                                             # return list to allfiles statment??? hence the loop???
 #  end of function "getlistoffiles"                            # I am just still understanding what is happening here.
                                                                # will come back and explain as I learn.

# begin of "copyfileobj(fsrc, fdst, length=16*1024)
#def copyfileobj(fsrc, fdst, length=16*1024):           # copy data from file-like object fsrc to file-like object fdst
 #   while 1:
  #      buf = fsrc.read(length)
   #     if not buf:
    #        break
     #   fdst.write(buf)
# end of "copyfileobj(fsrc, fdst, length=16*1024)

# begin function "writetofiles"(((untested)))
def writetofiles(list):
    wait = input("PRESS ENTER TO CONTINUE.")
    if os.path.isfile(temp_file):                               # if file(is there) is true or false
        # print ("File exists")                                 # if true print file exists
        with open(temp_file, 'rb') as rf:                       # open temp_file as rf, note if more then one string will get error

            for path in tqdm(list):
                rf.seek(0)
            # for path in list:                                   # call each string in list path
                with open(path,"wb") as wf:                     # open each string as wf
                    print (path)
                    # wf.seek(0)
                    shutil.copyfileobj(rf, wf)                         # call copyfileobj(fsrc, fdst length=16*1024) to write
                                                                # to files with a buffer in mind
    else:                                                       # or else
        print ("The Temp File is Missing")                      # print the temp file is missing
# end function "writetofiles"

# As I don't want every file made to 300mb, I need to filter files that we want to write to and leave a list ready
# for writing strings of files that I do want writen to.
# begining filter_video_exts(list) function (((tested)))
def filter_video_exts(a_list):

    for str in a_list:                                                      # for each string in list
        b_list = [s for s in a_list if any(sub in s for sub in (video_exts))] # make a list of string from eccepted list, i need further nots on this.
        # print(b_list)
        a_list = b_list
        # print(a_list)
        # print("filtered ready to pass to main")
        return a_list              # return list to main
#end filter_video_exts(list) function

# Begin ignore_these_files(listoffiles01)
def um_ignore_these_files(c_list):
    for str in c_list:
        # print(c_list)
        # print("check, check")
        d_list = [s for s in system_file_ignore if any(sub in s for sub in (c_list))]
        # print(d_list)
        C_list = d_list
        # print(c_list)
        # print("ignore ready to pass to main")
        # print(system_file_ignore)
        # list_check = True
        # for item in system_file_ignore:
        #     if item in c_list:
        #         continue
        # else:
        #     list_check = False
        #     break
        # print(list_check)
        return c_list
# if any string in this_list:
# maches any part of a string in that_list.
# remove sring from that list
# end

# This were everything comes together.
# begin executable function "main" (((not finnished))) um, almost ready for clean up.
def main():
    dirname = os.getcwd()                               # get directory of this module(python script) make it a string

    listoffiles01 = []                                  # Define list listoffiles01 empty list
    listoffiles01 = getlistoffiles(dirname)             # step one. populate "listoffiles01" list with "getlistoffiles(dirname)"
                                                        # function with strings.
    # print (listoffiles01)                               # test print listoffiles01
    # print ("---------->raw list")                          # "raw list success" print to console so we can see whats going on.
    # wait = input("PRESS ENTER TO CONTINUE.")            # this is just to stop the module(python script)

    listoffiles02 = []                                  # define list listoffiles02 empty list
    listoffiles02 = filter_video_exts(listoffiles01)    # step two. populate list with "filter_video_exts(listoffiles01)
    # print(listoffiles02)                                # function with strings.
    # listoffiles01 = listoffiles02                       # populate listoffiles02 with listoffiles01, note that
    # print(listoffiles02)
    # print ("--------->filtered list")
    # wait = input("PRESS ENTER TO CONTINUE.")                                                    # listoffiles01 will lose what strings it had in order to

    listoffiles03 = []
    listoffiles03 = um_ignore_these_files(listoffiles02)
    # listoffiles01 = listoffiles03                       # populate from listoffiles02 this way.
    # print (listoffiles03)                               # test print listoffiles02
    # print("---->removed ignored from list")             # "filter list success" print to console so we can see whats going on.
    # print("ignored system files")
    # wait = input("PRESS ENTER TO CONTINUE.")            # this is just to stop the module(python script)

    # print(listoffiles01)
    print("ready for writing files")
    wait = input("PRESS ENTER TO CONTINUE.")
    writetofiles(listoffiles03)                         # finish with writing to the files

if __name__ == '__main__':                              # If statement to check if main function is conditional.
    main()                                              # Invoke the main function
# end executable function "main"

# What i did was grabed code form googling and pieced it together, myself. If i had little
# to no understanding at all then nothing would work right? So you could in a way call
# this jumping in and learning to swim. lots of reading and playing around with code.
# I take little responce of doing the all the coding on my own.
# But i am responsible for putting code in this file and making it work, um mostly.
# Put together by Shawn D Quintal @ snowcatman@gmail.com and https://www.facebook.com/snowcatman
# I can be found on irc at times.(note: if you are waiting for me there you might be waiting a long while.
# As i am randomly online at time. However there are people there that can help you. google and read up on python first
# and don't worry about making mistakes. Ask question even if you don't get it, how to code in python.
# You will get better as you go. become familiar with what you are looking at. just my suggestion.
# so you might want to let me know your going to be there way in advanced if you want to chat with me.)
# in irc.freenode.net in (channel #python) making a fool of myself look for snowcatman
# On a serious note: a few people in the irc channel have shown me code.
# look for them and kindly think of there answer's before asking your questions again.
# I myself am learning that the hard way. I was able to go back and look at my channel logs for the chat
# and give these people at least some credit and reevaluate the advice they gave me.

# people with the nicknames are: <energizer> <jbowen> <jfhbrook> <offby1> <offby1> <varesa> <tech2> <Masakari>
# <moaz> <ikanobori> <han-solo> <moaz> <bjs> <Wooble> <Habbie> <metrognome> <nedbat> <noln> <altendky>

# Again, Thank You to those that put up with me. :-)
# this is part of files -- Goals_and_software_notes.txt -- shawn @ snowcatman@gmail.com

# If you read this far and are inclined to be helping me.
# Please add yourself down here to get credit. resend me a copy. please.
# chris cquintal@gmail.com knows a bit of java code, was able to help me with another file and i used parts of that file
# here. he helped me with a little bit of structure, for not knowing a hole lot of python. something tells me he
# knows more then he lets on.
# .

# end of file.