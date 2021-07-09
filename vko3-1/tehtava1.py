import requests
from google.cloud import storage

#Below is a Powershell command to set the environment variable for correct credentials key
#Create a service account and download the key, set the full path with filename to this path.
#$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

#Create a bucket, the service account key specifies the correct project.
def create_a_bucket(bucketname):
    storage_client = storage.Client()
    storage_client.create_bucket(bucketname)

#Uploads a file to given bucket by name, file is name by blobname, specified file is given as filename.
#The service account key specifies the correct project.
def upload_a_file(bucketname, blobname, my_filename):
    storage_client = storage.Client()
    my_bucket = storage_client.bucket(bucketname)
    my_blob = my_bucket.blob(blobname)
    my_blob.upload_from_filename(my_filename)

#Get the JSON
data_to_be_read = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
json_data = data_to_be_read.json()
data_items = json_data["items"]

#Write the file
try:
    file_to_be_opened = open("checkpoint.txt", "w")
    for x in data_items:
        file_to_be_opened.write(x["parameter"] + "\n")
    file_to_be_opened.close()
except:
    print("Something went wrong!")

#Create a bucket and upload the just created file there.
create_a_bucket("ilkkastestbucketcheckp3")
#Why did the instructions say the file had to be named checkpoint1? Funny thing.
upload_a_file("ilkkastestbucketcheckp3", "checkpoint1", "checkpoint.txt")

#This concludes first part.