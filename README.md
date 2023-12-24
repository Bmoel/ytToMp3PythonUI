# YT to MP3 Python UI
Simple program to copy in youtube URL and start youtube-dl command to download songs to that folder in an mp3 format.

## How to run
If you are on a windows device, you can simply download the program that is listed in the current Release. This is an exe that can run on your machine  
### Prerqeuisites to run
Download the following programs:
1) FFMPEG: https://ffmpeg.org/
2) youtube-dl: https://github.com/ytdl-org/youtube-dl  

For youtube-dl, use the following steps:
1) Download the latest youtube-dl exe from the nightly build repo: https://github.com/ytdl-org/ytdl-nightly
2) Put that exe in the folder of your choosing, and make sure to add that folder to your path (AKA the program should be able to be run globally in cmd line)

Note that FFMPEG also needs to be globally available, but the instructions on their site make it very easy to download with winget.

## Where to store the ytToMP3.exe file
The program will download the song files into the same directory that your program is in. So I would recommend placing the program wherever you will store your songs.

## How to install yourself 
1) Run `pip install pyinstaller`
2) cd one step outside of repository
3) Run the following `pyinstaller -F ./ytToMp3PythonUI/main.py`
4) The resulting exe will be inside of the dist folder generated
### Dependencies
1) pyinstaller -> `pip install pyinstaller`
2) PySimpleGUI -> https://www.pysimplegui.org/en/latest/#install
3) May need to install tkinter -> `pip install tk`

Note that if you are running this on ubuntu, I had some trouble with tkinter dependencies that got fixed by this:
https://www.pythonguis.com/installation/install-tkinter-linux/
I found that installing on windows was easier, but both should work fine