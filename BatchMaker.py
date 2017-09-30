# video-transcode-batch-script
#
# Copyright (c) 2017 Steven Phillips
import os
import sys
import subprocess

InputPath = 'Z:\Series\Star Trek Voyager\Season 1' #Set Input Path f.x. C:\movies NOT C:\movies\
print('Input Path: ' + InputPath + '...')
OutputPath = '"/absolute/path/to/outputs"' #Set Output Path. 
BatchScriptName = 'batch.sh' #Set based on your preference. f.x. 'batch.bat' for Windows
VideoTypeFilter = '.mkv' #Set based on which video type you want
SubtitleEngDetect = b'English (iso639-2: eng)' #Must start with 'b' 

with open(BatchScriptName, "w") as a: #Open the script
    for path, subdirs, files in os.walk(InputPath): #Walk the file path.
       for filename in files:
          if filename.endswith(VideoTypeFilter): #Filter file types by VideoTypeFilter.
            f = os.path.join(path, filename)
            print('Now Processing: ' + f)
            output = subprocess.check_output('transcode-video --scan ' + '"' + str(f) + '"' , shell=True) #Check for subtitles
            if b'English (iso639-2: eng)' in output: #If English subtitle is detected in scan output. Change 'English' and 'eng' to preferred language.
               EngSubs = ' --add-subtitle eng '
               print('English subtitle found, adding...')
            else:
               EngSubs = ''
               print('No subtiles found.')
            a.write('transcode-video' + EngSubs + '--target 1080p=8000 --quick --output ' + OutputPath + ' "' + str(f) + '"\n') #Set arguments for transcode-video. Change as needed. Each line must start with 'call' when using Windows. f.x. 'call transcode-video...'
