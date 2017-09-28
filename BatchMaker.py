import os
import sys

#Set Input Path f.x. C:\movies\
InputPath = '/absolute/path/to/inputs'
#Set Output Path. 
OutputPath = '"/absolute/path/to/outputs"'
#Set based on your preference. f.x. 'batch.bat' for Windows
BatchScriptName = 'batch.sh'
#Set based on which video type you want
VideoTypeFilter = '.mkv'

with open(BatchScriptName, "w") as a:
    for path, subdirs, files in os.walk(InputPath):
       for filename in files:
          if filename.endswith(VideoTypeFilter):
            f = os.path.join(path, filename)
            #Set agruments for transcode-video. Change as needed. Each line must start with 'call' when using Windows. f.x. 'call transcode-video...'
            a.write('transcode-video --target 1080p=8000 --quick --output ' + OutputPath + ' "' + str(f) + '"' + os.linesep) 
