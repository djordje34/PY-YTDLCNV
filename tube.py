import io
import os
import webbrowser
from urllib import request

from pytube import YouTube
from moviepy.editor import *
videos = []
f = open("urls_to_videos_go_here.txt", 'r')
for line in f:
    #videos.append(line.strip())
    link = line.strip()
    yt = YouTube(link)

    #Showing details
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)
    #Getting the highest resolution possible
    video = yt.streams.filter(only_audio=True).first()
    ys = yt.streams.get_highest_resolution()

    #Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")