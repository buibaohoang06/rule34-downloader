import urllib.request
import json
import os
import wget
import sys
import time


print("""
=======================================================================================
=                         Rule34 Image Downloader CLI. v1.0.0                         =  
=======================================================================================

! MAKE SURE TO PLACE THE SCRIPT INSIDE THE FOLDER YOU WISH TO INSTALL THE IMAGES INTO !
""")

try:
    print("[Info] > Please enter all the required information below: ")
    tag = input("[Info] > Enter the tag (if there are multiple, seperate them with a space): ")
    #Gather info from tag
    print("\n[Info] > Communicating with Rule34 server...")
    query_string = tag.replace(" ", "%20")
    print("[Info] > Gathering info with tag: " + tag)
    with urllib.request.urlopen(f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={query_string}&json=1') as data:
        json_data = json.loads(data.read().decode())

    
    print("[Info] > Gathering info complete!\n")
    print(f"[Info] > Found {str(len(json_data))} results with the tags '{tag}'\n")
    print("[Info] > Starting download script...")
    print("[Warning] > The script will keep downloading images that it can find, press Ctrl + C to stop when the desirable amount is met.")
    time.sleep(5)
    count = 0
    for i in range(0, len(json_data)):
        if os.path.exists(json_data[i]['image']):
            continue
        else:
            count = count + 1
            print(f"[Info] > Downloading #{count}: " + json_data[i]['hash'] + "\n")
            wget.download(json_data[i]['file_url'], os.getcwd())
            print("\n")
            time.sleep(1)
    print("\n[Info] > Download completed!")
    sys.exit("\nProgram ran with 0 errors.")
except KeyError:
    print("[Error] > Cannot find images with the provided keywords.")
except Exception as e:
    print("[Error] > " + str(e))
