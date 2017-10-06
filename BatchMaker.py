# video-transcode-batch-script
# Copyright (c) 2017 Steven Phillips
import os
import sys
import subprocess

InputPath = input("Enter the input path of your videos: ")#'Z:\Series\Star Trek Voyager\Season 1' #Set Input Path f.x. C:\movies NOT C:\movies\
OutputPath = input("Enter the output path of your videos: ") #Set Output Path. 
BatchScriptName = 'batch.sh' #Set based on your preference. f.x. 'batch.bat' for Windows
VideoTypeFilter = '.mkv' #Set based on which video type you want
SubtitleEngDetect = b'English (iso639-2: eng)' #Must start with 'b'

#Error checking
assert os.path.exists(InputPath), str(InputPath) + ' is not a valid path.' 
assert os.path.exists(OutputPath), str(OutputPath) + ' is not a valid path.'
if InputPath == OutputPath: 
   sys.exit('Input path must be different than output path')

print('Using Input Path: ' + InputPath + '...')
with open(BatchScriptName, "w") as a: #Open the script
    for path, subdirs, files in os.walk(InputPath): #Walk the file path.
       for filename in files:
          if filename.endswith(VideoTypeFilter): #Filter file types by VideoTypeFilter.
            TotalFiles = os.path.join(path, filename)
            print('Now Processing: ' + str(TotalFiles))
            output = subprocess.check_output('transcode-video --scan ' + '"' + str(TotalFiles) + '"' , shell=True) #Check for subtitles
            if b'English (iso639-2: eng)' in output: #If English subtitle is detected in scan output. Change 'English' and 'eng' to preferred language.
               EngSubs = ' --add-subtitle eng '
               print('English subtitle found, adding...')
            else:
               EngSubs = ''
               print('No subtiles found.')
            a.write('transcode-video' + str(EngSubs) + '--target 1080p=8000 --quick --output ' + '"' + str(OutputPath) + '"' + ' "' + str(TotalFiles) + '"\n') #Set arguments for transcode-video. Change as needed. Each line must start with 'call' when using Windows. f.x. 'call transcode-video...'
            print('Completed')
print('Process completed. ' + BatchScriptName + ' has been written to disk.')
