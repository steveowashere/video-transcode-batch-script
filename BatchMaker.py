# video-transcode-batch-script
#
# Copyright (c) 2017 Steven Phillips
#
import os
import sys
import subprocess

#Set Input Path f.x. C:\movies NOT C:\movies\
InputPath = '/absolute/path/to/inputs'
print('Processing ' + InputPath + '...')
#Set Output Path. 
OutputPath = '"/absolute/path/to/outputs"'
#Set based on your preference. f.x. 'batch.bat' for Windows
BatchScriptName = 'batch.sh'
#Set based on which video type you want
VideoTypeFilter = '.mkv'

SubtitleEngDetect = b'English (iso639-2: eng)' #Must start with 'b' 

with open(BatchScriptName, "w") as a: #Open the script
    for path, subdirs, files in os.walk(InputPath, topdown=True): #Walk the file path
       for filename in files:
          if filename.endswith(VideoTypeFilter): #Filter file types
            f = os.path.join(path, filename)
            print('Now Processing: ' + f)
            output = subprocess.check_output('transcode-video --scan ' + '"' + str(f) + '"' , shell=True) #Check for subtitles
            if b'English (iso639-2: eng)' in output: #If English subtitle is detected in scan output
               EngSubs = ' --add-subtitle eng '
               print('English subtitle found, adding...')
            else:
               EngSubs = ''
               print('No subtiles found.')
            #Set agruments for transcode-video. Change as needed. Each line must start with 'call' when using Windows. f.x. 'call transcode-video...'
            a.write('transcode-video' + EngSubs + '--target 1080p=8000 --quick --output ' + OutputPath + ' "' + str(f) + '"' + os.linesep)
            
