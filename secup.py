############### TITLE ##############
# This tool is made to share files/folders quickly with [curl] and [0x0.st]
# The main purpose of this script is to get a folder/file as [argc[1]], move it to temp dir argc[2]. zip it with a password from [argc[3]] then upload it to 0x0.st
# The stdout of the script is the link to the file
# PROGRAM PATH_TO_FILE_OR_FOLDER_TO_UPLOAD 
####################################

import os, subprocess, sys, uuid

TEMP_DIR = ""



def create_temp_dir():
    global TEMP_DIR
    # Check if argc[3] exists, so if a custom temp dir is given, if not, use /tmp
    if(len(sys.argv) == 3):
        TEMP_DIR = sys.argv[2]
    else:
        TEMP_DIR = "/tmp/secup"
    
    # Create directory to work in a separated space
    return_code = subprocess.run(['mkdir',TEMP_DIR], capture_output=True, text=True)
    
    # Basic error handling
    if(return_code.returncode == 1):
        print(f"Error while creating temp directory: \n{return_code.stderr}")

def collect_files_at_temp(TEMP_DIR_PATH):
    FILE_NAME = sys.argv[1]
    IS_IT_DIR = os.path.isdir
    if(IS_IT_DIR):
        return_code = subprocess.run(['cp','-r',FILE_NAME,TEMP_DIR_PATH], capture_output=True,text=True)
    else:
        return_code = subprocess.run(['cp',FILE_NAME,TEMP_DIR_PATH],capture_output=True,text=True)
    if(return_code.returncode == 1):
        print(f"Error happened while moving files: \n{return_code.stderr}")
    

def zip_collected_files():
    ZIP_PASS = sys.argv[3]
    ZIP_FILE_NAME = create_filename()
    return_code = subprocess.run(['zip','-p',ZIP_PASS,ZIP_FILE_NAME+".zip",TEMP_DIR+"/"])

    
def create_filename():
    UUID = str(uuid.uuid1()).split('-')[0]
    return (UUID)

if(__name__ == "__main__"):
    collect_files_at_temp("/tmp/secup")
    