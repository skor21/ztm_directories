# Ask user of program to specify url, then open file with common dir names, and we will read from the
# file and for each dir name wea re going perform request for that page. if we receive response or are able to load that
# page it means that directory exists on that page. If we get connection error, it means that page doesn't exist.

import requests  # Importing the requests library

target_url = input('[*] Enter target url: ')  # Asking the user of the program for target url
file_name = input('[*] Enter name of the File containing directories: ')  # We also ask for the file name


def request(url):
    try:
        return requests.get('http://' + url)  # If we manage to connect to url, will return this value inside the
    # response variable
    except requests.exceptions.ConnectionError:
        pass  # If we don't connect, response will stay empty


file = open(file_name, 'r')  # Open the file
for line in file:  # Read each and every line inside that file
    directory = line.strip()  # Strip it of any additional characters and store it inside the directory variable
    full_url = target_url + '/' + directory  # Then we create a full url variable that will be combination of target
    # url and directory name
    response = request(full_url)  # We request that full url
    if response:  # If there is something in the response  print that we discovered directory at path, if nothing
        # it will not print anything.
        print('[*] Discovered directory at this path: ' + full_url)

# We can also search subdirectories: Instead of typing 192.168.1.101 we can type 192.168.1.101/dvwa
# Successfully performed using the common.txt file located in Kali $ cd usr/share/dirb $ cd wordlists $ common.txt
