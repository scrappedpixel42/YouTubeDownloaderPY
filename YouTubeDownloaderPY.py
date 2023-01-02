# ################################################################
# #                                                              #
# #            Project ID    : YT02FP1                           #
# #            Project Name  : YouTube Downloader PY             #
# #            Author        : scrappedpixel42                   #
# #            Date-initiated: 12-7-2022                         #
# #            Date-updated  : 12-10-2022                         #
# #                                                              #
# ################################################################
# #    An efficient YouTube downloader that is downloads the     #
# #    the selected URL(s) at the highest resolution to a 	     #
# #    chosen directory.                                         #
# ################################################################
from pytube import YouTube
from pytube.cli import on_progress
import keyboard
import os
import time

# ################################################################
# #                          Variables                           #
# ################################################################
"""Version""" 
version_         = "v0.4.87"

"""Software Information"""
author          = "By scrappedpixel42"
code_one_desc   = "Invalid YouTube URL!"
code_zero_desc  = "Invalid directory!"
description     = ["This is an easy and free to use ",
                   "YouTube downloader program. Copy",
                   "and paste a YouTube URL, find a ",
                   "valid directory, and download   ",
                   "the video in seconds.           "]
err_code_one    = "1"
err_code_zero   = "Error Code: 00"
software_title  = "YouTube Downloader PY"

"""Placeholders and Numbers"""
asset           = "#"
#chunk           = 1024
column          = 96
row             = 14

# ################################################################
# #                          Functions                           #
# ################################################################
"""Tools"""
def custom_center(text):
    t = text.center(column - 2)
    print(asset + t + asset, end="")

def dotmove(n):
    dot = "."*n
    loading = (f"Loading{dot}")
    print(loading + " ", end = '\r')
    time.sleep(1)
    
def download_(yt_link, PATH):
    x = yt_link.streams.get_highest_resolution()
    x.download(PATH)
    
def path_check():
    alt_row_1 = 5
    alt_row_2 = 6
    print("\n\n")
    while True:
        tabin()
        text = input("Enter a valid directory: ")
        print("\n\n\n")
        directory = os.path.isdir(text)
        if(directory == True):
            for y in range(1, alt_row_1 + 1):
                tabin()
                for x in range(1, column + 1):
                    if(y == 1 or y == alt_row_1 or
                       x == 1 or x == column):
                        if(y == 3):
                            custom_center("Valid directory!")
                            break
                        print(asset, end="")
                    else:
                        print(" ", end="")
                print()
            print("\n\n")
            break
        else:
            for y in range(1, alt_row_2 + 1):
                tabin()
                for x in range(1, column + 1):
                    if(y == 1 or y == alt_row_2 or
                       x == 1 or x == column):
                        if(y == 3):
                            custom_center(err_code_zero)
                            break
                        if(y == 4):
                            custom_center(code_zero_desc)
                            break
                        print(asset, end="")
                    else:
                        print(" ", end="")
                print()
            print("\n\n")
            continue
    return text

def reload_(y, x):
    if(y != x):
        os.system('cls')
        title_screen()
        y = x
        
def startup_():
    for element in range(4):
        dotmove(element)
    os.system('cls')

def tabin():
    line = ""
    variable = os.get_terminal_size().columns
    e = int((variable - column) / 2)
    for i in range(1, e + 1):
        line += " "
    print(line, end="") 

def title_screen():
    n = 0
    print("\n\n\n")
    for i in range(1, row + 1):
        tabin()
        for e in range(1, column + 1):
            if(i == 1 or i == row or  
               e == 1 or e == column):
                if(i == 2):
                    version(version_)
                    break
                if(i == 4):
                    custom_center(software_title)
                    break
                if(i == 6):
                    custom_center(author)
                    break
                if(i >= 9 and i <= 12):
                    custom_center(description[n])
                    n += 1
                    break
                print(asset, end="")
            else:
                print(" ", end="")
        print()
    print("\t\t\t")  

"""   
Function Does not work 
def youtube_url_validation(text):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, text)
    if youtube_regex_match:
        return True

    return False
"""
    
def version(text):
    v = column - (len(text) + 3)
    print(asset, end="")
    for element in range(v):
        print(" ", end="")
    print(version_ + " " + asset, end="")

"""
Requires youtube_url_validation function to work
def video_check(text):
    alt_row_2 = 6
    print("\n\n\n")
    if (youtube_url_validation(text) != True):
        for y in range(1, alt_row_2 + 1):
            tabin()
            for x in range(1, column + 1):
                if(y == 1 or y == alt_row_2 or
                   x == 1 or x == column):
                    if(y == 3):
                        custom_center(err_code_one)
                        break
                    if(y == 4):
                        custom_center(code_one_desc)
                        break
                    print(asset, end="")
                else:
                    print(" ", end="")
            print()
        print("\n\n")
    else:
        video_info(text)
"""
        
def video_info(text):
    alt_row = 6
    print("\n\n")
    yt = YouTube(text)
    for y in range(1, alt_row + 1):
        tabin()
        for x in range(1, column + 1):
            if(y == 1 or y == alt_row or
               x == 1 or x == column):
                if(y == 3):
                    custom_center(yt.title)
                    break
                if(y == 4):
                    custom_center(yt.author)
                    break
                print(asset, end="")
            else:
                print(" ", end="")
        print()
    print("\n\n")
        
# ################################################################
# #                             Main                             #
# ################################################################
g = os.get_terminal_size()
n = os.get_terminal_size()
startup_()
while True:
    title_screen()
    g = os.get_terminal_size()
    reload_(n, g)
    
    tabin()
    PATH = path_check()
    
    tabin()
    link = input("Enter a valid YouTube URL: ")
    
    tabin()
    video_info(link)
    
    yt = YouTube(link, on_progress_callback=on_progress)
    print("\t\t\t", end="")
    download_(yt, PATH)
    
    input()
    
    # Reruns program based on user input.
    os.system('cls')
    answer = int(input("Run again? (Press 1 for yes / 0 for no): "))
    if(answer == 1):
        os.system('cls')
        continue
    else:
        print("Shutting down", end="")
        for t in range(4):
            time.sleep(1)
            print(".", end="")
        break
        
        