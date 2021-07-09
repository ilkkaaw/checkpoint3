import requests

data_to_be_read = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
json_data = data_to_be_read.json()
data_items = json_data["items"]

try:
    file_to_be_opened = open("checkpoint.txt", "w")
    for x in data_items:
        file_to_be_opened.write(x["parameter"] + "\n")
    file_to_be_opened.close()
except:
    print("Something went wrong!")