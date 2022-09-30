import urllib.request
import json
import os
import wget
import sys

print("""
=======================================================================================
=                         Rule34 Image Downloader CLI. v0.0.1                         =  
=======================================================================================

! MAKE SURE TO PLACE THE SCRIPT INSIDE THE FOLDER YOU WISH TO INSTALL THE IMAGES INTO !
""")

try:
    print("> Please enter all the required information below: ")
    tag = input("> Enter the tag (if there are multiple, seperate them with a ',' no spaces): ")
    limit = input("> Number of images: ")
    #Gather info from tag
    print("\n> Communicating with Rule34 server...")
    query_string = tag.replace(",", "%20")
    print("Gathering info with tag: " + tag)
    with urllib.request.urlopen(f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={query_string}&json=1&limit={limit}') as data:
        json_data = json.loads(data.read().decode())

    images = []

    for i in range(0, len(json_data)):
        images.append(json_data[i]['file_url'])
    print("> Gathering info complete!\n")
    print(f"> Found {str(len(json_data))} results out of {limit} set by user with the tags '{tag}'\n")
    print("> Starting download script...")
    for links in images:
        wget.download(links, os.getcwd())
    sys.exit("> Download completed!")
except Exception as e:
    print("> Error occured: " + str(e))
