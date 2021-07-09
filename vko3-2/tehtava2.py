import argparse
from google.cloud import storage
import os.path
import time

#Below is a Powershell command to set the environment variable for correct credentials key
#Create a service account and download the key, set the full path with filename to this path.
#$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

#Downloads a file from given bucket by name, file is name by whattodl, howtonameit is the filename in the system it is downloaded to (local computer).
#The service account key specifies the correct project.
def download_a_file(bucketname, whattodl, howtonameit):
    storage_client = storage.Client()
    my_bucket = storage_client.bucket(bucketname)
    my_blob = my_bucket.blob(whattodl)
    my_blob.download_to_filename(howtonameit)

#Add the argument, lines to be read.
parser = argparse.ArgumentParser(description="Requires a number as argument to read that many lines from the checkpoint text file")
parser.add_argument("lineamount", help="Amount of lines to be read")
args = parser.parse_args()

#Download the file.
download_a_file("ilkkastestbucketcheckp3", "checkpoint1", "checkpoint.txt")
#Wait until it exists.
while not os.path.exists("checkpoint.txt"):
    time.sleep(1)

#Okay, it should exist now.
if os.path.isfile("checkpoint.txt"):
    try:
        #Open the file
        opened_file = open("checkpoint.txt", "r")
        all_lines = opened_file.readlines()
        #Take the argument and take just that many lines
        modified_list = all_lines[:int(args.lineamount)]
        #Remove newline
        stripped_list = [item.strip("\n") for item in modified_list]
        #Sort by length
        sorted_list = sorted(stripped_list, key=len)
        #Print
        for x in sorted_list:
            print(x)
        opened_file.close()
    #Try-except just for future modifiability
    except:
        print("Something went wrong!")

#This concludes second part.