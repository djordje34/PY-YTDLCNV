from pydub import AudioSegment
from moviepy.editor import *
import glob
import os.path

dir = '.'
allfiles = os.listdir(dir)
files = [ fname for fname in allfiles if fname.endswith('.mp4')]
print(files)
for file in files:
    video = VideoFileClip(file)
    video.audio.write_audiofile("converted/"+file.split('mp4')[0]+'mp3')
