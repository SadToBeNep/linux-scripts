############### TITLE ##############
# This tool is made to share files/folders quickly with [curl] and [0x0.st]
# The main purpose of this script is to get a folder/file as [argc[1]], then upload it to 0x0.st
# The stdout of the script is the link to the file
#
# 0x0.st is a simple website where I can upload my files
# in case I want to share something with someone
# and for example the file would be too big for a discord share,
# or I just simply want to save a file
# for later use somewhere else on another computer
#
#
#
# PROGRAM PATH_TO_FILE_OR_FOLDER_TO_UPLOAD
####################################
"""Modules to execute commands"""
import os
import subprocess
import sys
import uuid

TEMP_DIR_PATH = "/tmp/secup"


def create_temp_dir():
    """Creates temp directory"""

    # Create directory to work in a separated space
    return_code = subprocess.run(['mkdir', TEMP_DIR_PATH],
                                 capture_output=True, text=True, check=False)

    # Basic error handling
    if return_code.returncode == 1:
        print(f"Error while creating temp directory: \n{return_code.stderr}")


def collect_files_at_temp():
    """Collect files in one place"""

    create_temp_dir()
    file_name = sys.argv[1]
    is_it_dir = os.path.isdir
    if is_it_dir:
        return_code = subprocess.run(['cp', '-r', file_name, TEMP_DIR_PATH],
                                     capture_output=True, text=True, check=False)
    else:
        return_code = subprocess.run(['cp', file_name, TEMP_DIR_PATH],
                                     capture_output=True, text=True, check=False)

    if return_code.returncode == 1:
        print(f"Error happened while moving files: \n{return_code.stderr}")
    else:
        zip_collected_files()


def zip_collected_files():
    """Zip the collected files"""

    zip_file_name = create_filename()
    return_code = subprocess.run(['zip', '-r', '-e', zip_file_name+".zip", TEMP_DIR_PATH+"/"],
                                 capture_output=True, text=True, check=False)
    print(return_code)
    if return_code.returncode == 1:
        print(f"Error: \n{return_code.stderr}")
    upload_zip_file(zip_file_name)


def upload_zip_file(ZIP_FILE_NAME):
    """Upload the created zip file"""

    lcg = TEMP_DIR_PATH+"/"+ZIP_FILE_NAME+".zip"

    subprocess.run(['mv', ZIP_FILE_NAME+".zip", TEMP_DIR_PATH+"/."],check=False)
    return_code = subprocess.run(['curl', '-F', f"file=@{lcg}", 'http://0x0.st'],
                                 capture_output=True, text=True, check=False)
    print(return_code.stdout)
    cleanup()


def cleanup():
    """Cleanup so if the program is run again,
      does not miss/upload files by mistake from prev run"""
    subprocess.run(['rm', '-rf', TEMP_DIR_PATH], check=False)


def create_filename():
    """Randomly generates file name"""
    uuid_gen = str(uuid.uuid1()).split('-',maxsplit=1)[0]
    return uuid_gen


if __name__ == "__main__":
    collect_files_at_temp()
