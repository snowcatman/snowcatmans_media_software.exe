import os
import sys
import logging
from shutil import copyfile
import subprocess

logging.basicConfig(filename="converting.log", level=logging.DEBUG)
logging.debug("Starting Logging")

walk_dir = sys.argv[1]
copy_to_dir = sys.argv[2]

print('walk_dir = ' + walk_dir)
print('copy_to_dir = ' + copy_to_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
walk_dir = os.path.abspath(walk_dir)
copy_to_dir = os.path.abspath(copy_to_dir)

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
print('copy_to_dir (absolute) = ' + os.path.abspath(copy_to_dir))

for root, subdirs, files in os.walk(walk_dir):
    count = 0
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)

    copy_to = copy_to_dir+root[len(walk_dir):]
    print('copy_dir = ' + copy_to)
    try:
        os.mkdir(copy_to)
        logging.debug("Created dir: " +copy_to)
        print('Created dir: ' +copy_to)
    except:
        logging.debug("Failed to create dir: " +copy_to)
        print('Failed to create dir: ' +copy_to)
    
    with open(list_file_path, 'wb') as list_file:
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)

        for filename in files:
            
            file_path = os.path.join(root, filename)
            print('\t- file %s (full path: %s)' % (filename, file_path))
            logging.debug("Filename: "+filename)
            
            copy_file_to = copy_to + "/" +filename
            print("Copy from: " + file_path + " to: " + copy_file_to)
            
            try:
                print(file_path[-4:])
                if file_path[-4:].lower() == ".mkv":
                    copy_file_to = copy_file_to[:-4] + ".mp4"
                    count = count + 1
                    subprocess.check_output(['ffmpeg', '-i', file_path,
                                             '-f', 'mp4',
                                             '-vcodec', 'libx264',
                                             '-crf', '20', '-n',
                                             copy_file_to])
                    print("Converted " +count +" MKV: " +file_path)
                    logging.debug("Converted: " +copy_file_to)
                else:
                    copyfile(file_path, copy_file_to)
                    logging.debug("Copied: "+copy_file_to)
                    print("Copied: "+file_path)
            except:
                print("Failed to copy: "+file_path)
                logging.debug("Failed to Copy: "+file_path)