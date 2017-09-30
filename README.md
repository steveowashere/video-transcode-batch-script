# Transcode_Video Batch Script
A simple script to make batch scripts for [Transcode Video](https://github.com/donmelton/video_transcoding  "Transcode Video") by Don Melton

# About
I'm a huge fan of Transcode Video and use it on my media server, the one problem I faced was (semi)automating the process. For me in my workflow, I have an *intake* folder, and *finished_transcodes* folder and a *movies* folder (which Plex is using). So all my raw videos get dumped into the *intake* folder, Transcode_Video does its magic, and the videos are outputted to *finished_transcodes*. I then manually inspect each transcoded video and move them to the *movies* folder. This script is made for my workflow when dealing with large amount of similar videos like from ripping TV series, but it can also work in a few other cases. I hope it comes in handy.

If this isn't doesn't suit your needs, Don provides example for batch scripts. [See here.](https://github.com/donmelton/video_transcoding/blob/master/README.md#batch-control-for-transcode-video)

# Usage

There is one python script than needs to be run in whichever way you see fit (Python 3 is required). This depends on your OS. It has been tested on Linux and Windows. It will likely work on OSx.  The batch script will be output as a shell script by default, but this can be changed to any format needed by modifying the 'BatchScriptName'

The script also needs to be setup for your folders/paths.  You also need to manually enter the arguments you want for each video that will be processed. I have included my 'default' agruments I use. Pay attention to the comments in the script, as they will tell you what everything does.

Detecting and adding subtitles works, but it requires a little care. At the moment, it only looks for English subtitles using the 'transcode-video --scan' command. You can easliy change this to fit your language preference. To add more than one subtitle can be done by simply adding another if-else statement before writing the text. 

# Future Plans

* Better way to handle subtitles
* More things that come to mind
