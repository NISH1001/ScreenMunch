#!/bin/bash

echo "recording screen using ffcast..."

if [ -z "$1" ]; then
    echo "no output filename given. -_-"
    exit
fi 

echo "output file: '$1'"
# ffmpeg -f x11grab -r 15 -s 1366x768 -i :0.0 -vcodec huffyuv test.avi
# ffcast -www ffmpeg -f x11grab -show_region 1 -s %s -i %D+%c test.mp4
ffcast ffmpeg -f x11grab -show_region 1 -s %s -i %D+%c $1
