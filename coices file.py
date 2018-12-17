import os
import stat
import time
import sys
import re

clear = lambda: os.system('cls')
clear()
print()
print("Please make a choice")

def has_hidden_attripute(filepath):
    return bool(os.stat(filepath).st_file_attribute & stat.file_attribute_hidden)

choice = ''

while choice != 'q' and choice != '4':
    print("\n[1] Enter 1 to create a media text file.")
    print("[2] Enter 2 to no code yet, run empty task.")
    print("[3] Enter 3 to no code yet, run empty task.")
    print("[4] Enter q to Quit.")

    choice = input("\nWhat would you like to do? ")
    clear = lambda: os.system('cls')
    clear()




    if choice == "1":
        print("\nCreating medialist.txt\n")

        from timeit import default_timer as timer
        start = timer()

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


        def main():
            dirname = os.getcwd()
            # listoffiles = getlistoffiles(dirname)
            listoffiles = list()
            listOfTvShows = list()
            listOfMovies = list()

            # Pattern Matching Testing
            # line1 = "Superman 2010 [R]"
            # line2 = "Superman 2010"
            # line3 = "1900 Superman 2010 R"
            # line4 = "1900 2010 R"
            # line5 = "season1"
            # matchObj1 = re.match(r'^([a-z0-9A-Z ]+) (\d{4})(.*)', lin1e, re.I)
            # matchObj2 = re.match(r'^([a-z0-9A-Z ]+) (\d{4})(.*)', line2, re.I)
            # if(matchObj1 and matchObj2):
            # print("dir: ", matchObj1.group(1))
            # print("file: ", matchObj2.group(1))
            # print ("Same?: ", matchObj1.group(1) == matchObj2.group(1))
            # else:
            # print("No Match")
            # End Pattern Matching Testing

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

            f = open('medialist.txt', 'w')                                  #creat/over_write open file medialist.txt

            tv_output = "\n TV Shows, count: "+ str(len(listOfTvShows))
            f.write (tv_output)
            for elem in listOfTvShows:
                f.write('\n' + elem)

            movies_output = "\n Movies, count: "+ str(len(listOfMovies))
            f.write (movies_output)
            for elem in listOfMovies:
                f.write('\n' + elem)

            f.close()


        if __name__ == '__main__':
            main()


        end = timer()
        clear = lambda: os.system('cls')
        clear()
        print()
        print("Finnished in", end - start)
        time.sleep(3)
        clear = lambda: os.system('cls')
        clear()
        print("")
        print("please make another choice")


    elif choice == "2":

        print()
        print("\nworking choice 2\n")
        from timeit import default_timer as timer
        start = timer()
        # code goes here
        end = timer()
        clear = lambda: os.system('cls')
        clear()
        print()
        print("Finnished in", end - start)
        time.sleep(3)
        clear = lambda: os.system('cls')
        clear()
        print("")
        print("please make another choice")


    elif choice == "3":

        print()
        print("\nworking choice 3\n")
        from timeit import default_timer as timer
        start = timer()
        # code goes here
        end = timer()
        clear = lambda: os.system('cls')
        clear()
        print()
        print("Finnished in", end - start)
        time.sleep(3)
        clear = lambda: os.system('cls')
        clear()
        print("")
        print("please make another choice")


    elif choice == ("4") or ("q"):
        print("\nExiting\n")

    else:
        print("\nI don't understand that choice, please try again.\n")

clear = lambda: os.system('cls')
clear()
# print("----You should be at the command prompt. Thank you.----")
