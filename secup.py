############### TITLE ##############
# This tool is made to share files/folders quickly with [curl] and [0x0.st]
# The main purpose of this script is to get a folder/file as [argc[1]], then upload it to 0x0.st
# The stdout of the script is the link to the file
#
# 0x0.st is a simple website where I can upload my files in case I want to share something with someone
# and for example the file would be too big for a discord share, or I just simply want to save a file 
# for later use somewhere else on another computer
#
#
#
# PROGRAM PATH_TO_FILE_OR_FOLDER_TO_UPLOAD
####################################

import os, subprocess, sys, uuid
TEMP_DIR_PATH = "/tmp/secup"


def create_temp_dir():
    
    # Create directory to work in a separated space
    return_code = subprocess.run(['mkdir',TEMP_DIR_PATH], capture_output=True, text=True)
    
    # Basic error handling
    if(return_code.returncode == 1):
        print(f"Error while creating temp directory: \n{return_code.stderr}")

def collect_files_at_temp():
    create_temp_dir()
    FILE_NAME = sys.argv[1]
    IS_IT_DIR = os.path.isdir
    if(IS_IT_DIR):
        return_code = subprocess.run(['cp','-r',FILE_NAME,TEMP_DIR_PATH], capture_output=True,text=True)
    else:
        return_code = subprocess.run(['cp',FILE_NAME,TEMP_DIR_PATH],capture_output=True,text=True)
    if(return_code.returncode == 1):
        print(f"Error happened while moving files: \n{return_code.stderr}")
    else:
        zip_collected_files()
    

def zip_collected_files():
    ZIP_FILE_NAME = create_filename()
    return_code = subprocess.run(['zip','-r','-e',ZIP_FILE_NAME+".zip",TEMP_DIR_PATH+"/"],capture_output=True,text=True)
    print(return_code)
    if(return_code.returncode == 1):
        print(f"Error: \n{return_code.stderr}")
    upload_zip_file(ZIP_FILE_NAME)

def upload_zip_file(ZIP_FILE_NAME):
    LCG = TEMP_DIR_PATH+"/"+ZIP_FILE_NAME+".zip"
    
    subprocess.run(['mv',ZIP_FILE_NAME+".zip",TEMP_DIR_PATH+"/."])
    return_code = subprocess.run(['curl','-F',f"file=@{LCG}",'http://0x0.st'],capture_output=True,text=True)
    print(return_code.stdout)
    cleanup()

def cleanup():
    subprocess.run(['rm','-rf',TEMP_DIR_PATH])

    
def create_filename():
    UUID = str(uuid.uuid1()).split('-')[0]
    return (UUID)

if(__name__ == "__main__"):
    collect_files_at_temp()
    