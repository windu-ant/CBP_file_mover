import os
import fnmatch
import shutil

# Open and read the txt file
with open('profiles.txt', 'r') as f:
    profiles = f.readlines()

for profile in profiles:
    # Split the profile info
    profile_info = profile.split(':')
    profile_num = profile_info[0].split()[-1]  # get the number part
    name = profile_info[1].strip()  # get the name part

    # Split name into first and last names
    names = name.split()
    first_name = names[0]
    last_names = names[1:]
    formatted_name = ' '.join(last_names) + ', ' + first_name

    # set current working directoy to move files to
    cwd = os.getcwd()
    # one directory up
    parent_directory = os.path.join(cwd, '..')
    # sent backgrounds folder
    sent_backgrounds = os.path.join(parent_directory, '1 - Sent for Background check')

    # iterate to find folders
    directories = next(os.walk(sent_backgrounds))[1]

    # move to the desired folder based on name, builds dummy folder if not found
    dst_dir = None
    for directory in directories:
        if fnmatch.fnmatch(directory, formatted_name + '*'):
            dst_dir = os.path.join(sent_backgrounds, directory)
            shutil.move(dst_dir, cwd)
            print(sent_backgrounds + ' moved to CWD')
            break
    
    if not dst_dir:
        dst_dir = os.path.join(cwd, formatted_name + ' NOT_FOUND')
        os.makedirs(dst_dir, exist_ok=True)
        print(formatted_name + ' NOT FOUND')
    
input('Press enter to exit...')    